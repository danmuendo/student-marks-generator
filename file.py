from os import path
# import re
from random import choice
from typing import List


class FileResultHandler(object):

    BASE_DIR = path.dirname(__file__)

    def __init__(self, filename, number_of_students):
        self._filename = filename
        self._number_of_students = number_of_students

    def generate_marks(self):
        try:
            file_to_read = path.join(
                self.__class__.BASE_DIR,
                self._filename
            )
            file = open(file_to_read, "w")
            [file.write(f"{choice([x for x in range(1,100)])}\n")
             for index in range(self._number_of_students)]

        except Exception as e:
            print(e.with_traceback())
        finally:
            print("Done generating marks....")

    def read_marks(self,
                   passmark=20,
                   *args,
                   **kwargs
                   ):
        passed = 0
        not_passed = 0
        read = ""
        total_score = 0
        try:
            with open(self._filename, "r") as record:
                search = r"[0-9]+[\.0-9]*"
                searchable = record.read().strip()
                read += searchable.replace("\n", ",")
        except Exception as e:
            print(e.with_traceback())
        finally:
            print()
        read_mks = read.split(",")
        for mark in read_mks:
            converted = int(mark)
            if converted > passmark:
                passed += 1
            else:
                not_passed += 1
            total_score += int(converted)

        print(f"""
Passed students ------------- {passed}
Failed students ------------- {not_passed}
Total students -------------- {passed+not_passed}
Mean score ------------------ {total_score/len(read_mks)}
\n
        
        """.strip())
        print("Done reading marks.....")


students = FileResultHandler("marks.txt", 200)
students.generate_marks()
students.read_marks(passmark=60)
