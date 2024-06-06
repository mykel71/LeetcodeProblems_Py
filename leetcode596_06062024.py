import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    course_total = courses.groupby(['class']).count().reset_index()
    course_total_final = course_total[course_total['student'] > 5]
    return course_total_final[['class']]