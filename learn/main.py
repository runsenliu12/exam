import tensorflow as tf
from tensorflow import keras


import tensorflow as tf
from tensorflow import keras


class Din:
    # 定义多层感知机模型
    mlp = keras.Sequential(
        [
            keras.layers.Dense(60, activation=tf.nn.sigmoid, name="f1_att"),
            keras.layers.Dense(40, activation=tf.nn.sigmoid, name="f2_att"),
            keras.layers.Dense(1, activation=tf.nn.sigmoid, name="f3_att"),
        ]
    )

    @classmethod
    def attention(cls, ori_queries, keys, keys_length):
        """
        DIN 模型的注意力机制部分

        Parameters:
        - ori_queries: 用户当前的查询向量，形状为 [B, 1, H]，其中 B 是批处理大小，H 是查询向量的维度。
        - keys: 用户历史行为的键向量，形状为 [B, T, H]，其中 T 是历史行为序列的长度。
        - keys_length: 保存用户历史行为的真实长度，形状为 [B]。

        Returns:
        - output: 注意力加权后的键向量，形状为 [B, 1, H]。
        """

        # 复制查询向量，使其与键向量相同维度
        queries = tf.tile(ori_queries, [1, tf.shape(keys)[1], 1])

        # 将四个不同的特征拼接在一起
        din_all = tf.concat([queries, keys, queries - keys, queries * keys], axis=-1)

        # 通过多层感知机模型学习特征权重
        d_layers_3_all = cls.mlp(din_all)

        # 调整输出形状
        d_layers_3_all = tf.reshape(d_layers_3_all, [-1, 1, tf.shape(keys)[1]])
        output = d_layers_3_all

        # 生成键掩码
        key_masks = tf.sequence_mask(keys_length, tf.shape(keys)[1])
        key_masks = tf.expand_dims(key_masks, 1)
        paddings = tf.ones_like(output)

        # 根据键掩码对输出进行掩码处理
        output = tf.compat.v1.where(key_masks, output, paddings)

        # 缩放处理
        output = tf.divide(output, keys.get_shape().as_list()[-1] ** 0.5)

        # 使用 softmax 获得注意力权重
        output = tf.nn.softmax(output)

        # 进行加权求和得到最终输出
        output = tf.raw_ops.BatchMatMul(x=output, y=keys)

        return output


# Example usage
ori_queries_example = tf.constant([[[1.0, 2.0, 3.0]]])  # Shape: [1, 1, 3]
keys_example = tf.constant(
    [[[4.0, 5.0, 6.0], [7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]]
)  # Shape: [1, 3, 3]
keys_length_example = tf.constant([3])  # Shape: [1]

# Call the attention method
output_example = Din.attention(ori_queries_example, keys_example, keys_length_example)

# Print the output
print("Attention Output:")
print(output_example.numpy())
print(output_example.shape)


# Example usage
ori_queries_example = tf.constant(
    [[[1.0, 2.0, 3.0, 1.0, 2.0, 3.0]]]
)  # Shape: [1, 1, 6]
keys_example = tf.constant(
    [
        [
            [4.0, 5.0, 6.0, 1.0, 2.0, 3.0],
            [7.0, 8.0, 9.0, 1.0, 2.0, 3.0],
            [10.0, 11.0, 12.0, 1.0, 2.0, 3.0],
        ]
    ]
)  # Shape: [1, 3, 6]
keys_length_example = tf.constant([3])  # Shape: [1]

# Call the attention method
output_example = Din.attention(ori_queries_example, keys_example, keys_length_example)

# Print the output
print("Attention Output:")
print(output_example.numpy())
print(output_example.shape)
