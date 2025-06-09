job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel'],'remote':True},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning'],'remote':False},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn'],'remote':True},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL'],'remote':False},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel'],'remote':False},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics'],'remote':True},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement'],'remote':False},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management'],'remote':False},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision'],'remote':True},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling'],'remote':False}
]
ans=list(filter(lambda job:job['remote'] and 'Python' in job['skills'],job_roles))
print(ans)
