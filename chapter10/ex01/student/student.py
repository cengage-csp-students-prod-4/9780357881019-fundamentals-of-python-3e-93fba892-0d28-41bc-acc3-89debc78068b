"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """Constructor creates a Student with the given
        name and number of scores and sets all scores
        to 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverageScore(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self, other):
        """Tests for equality by comparing names."""
        return self.name == other.name

    def __lt__(self, other):
        """Tests for less than by comparing names."""
        return self.name < other.name

    def __ge__(self, other):
        """Tests for greater than or equal to by comparing names."""
        return self.name >= other.name

    def __str__(self):
        """Returns the string representation of the
        student."""
        return "Name: " + self.name + "\nScores: " + \
               ", ".join(map(str, self.scores))


def main():
    """Tests the comparison operators."""
    s1 = Student("Ken", 5)
    s2 = Student("Ann", 5)
    s3 = Student("Ken", 5)

    print("False:", s1 == s2)
    print("True:", s1 == s3)
    print("True:", s1 != s2)
    print("False:", s1 < s2)
    print("True:", s2 < s1)
    print("True:", s1 >= s2)
    print("True:", s1 >= s3)
    print("True:", s1 > s2)
    print("True:", s1 <= s3)
    print("True:", s2 <= s1)


if __name__ == "__main__":
    main()