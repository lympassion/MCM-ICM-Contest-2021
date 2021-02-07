def get_data(list):
    #use to show data
    data = []
    for single in list:
        country     = single[0]
        year        = single[1]
        grossEnrollmentRatio = single[2]
        expenditure          = single[3]
        # Government expenditure on education, total (% of GDP)
        percentageOfHigherEducation = single[4]
        amountOfColleges            = single[5]
        # Only count Top 100 colleges
        percentageOfInternationalStu = single[6]
        detail = {'country': country, 'year': year, 'grossEnrollmentRatio': grossEnrollmentRatio,
                  'expenditure': expenditure, 'percentageOfHigherEducation': percentageOfHigherEducation,
                  'amountOfColleges': amountOfColleges, 'percentageOfInternationalStu': percentageOfInternationalStu}
        data.append(detail)
    return data
