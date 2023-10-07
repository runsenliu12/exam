"""

示例 1：

输入：students = [1,1,0,0], sandwiches = [0,1,0,1]
输出：0
解释：
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [1,0,0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [0,0,1,1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [0,1,1]，三明治栈为 sandwiches = [1,0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [1,1,0]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [1,0]，三明治栈为 sandwiches = [0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [0,1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [1]，三明治栈为 sandwiches = [1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = []，三明治栈为 sandwiches = []。
所以所有学生都有三明治吃。
示例 2：

输入：students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
输出：3
 
"""
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                ### 判断有没有对应的
                if sandwiches[0] in students:
                    students.append(students.pop(0))
                else:
                    break
        return len(students)


if __name__ == "__main__":
    s = Solution()
    print(s.countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
    print(s.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
