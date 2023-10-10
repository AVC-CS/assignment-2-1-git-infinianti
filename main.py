def main():
    def input_message(gender: str): return f'How many {gender} students are in the class?\n'
    def percentage_message(gender: str): return f'The Perecentage of {gender} Students is:'
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    _gender = ('male', 'female')
    male = int(input(input_message(_gender[0])))
    female = int(input(input_message(_gender[1])))
    students = male + female
    m_perc = male / students
    f_perc = female / students

    print( f'\nThere are {students} students in the class!\n\n{percentage_message(_gender[0].capitalize())}\t{m_perc:.2%}\n{percentage_message(_gender[1].capitalize())}\t{f_perc:.2%}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc * 100, f_perc * 100


if __name__ == '__main__':
    main()
