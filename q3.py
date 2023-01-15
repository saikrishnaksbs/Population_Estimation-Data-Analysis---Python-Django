import csv
import matplotlib.pyplot as plt


def calculate(population):
    '''for calculating'''
    years = set()
    saarccountries = ['Afghanistan', 'Bangladesh', 'Bhutan',
                      'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri-Lanka']
    for people in population:
        years.add(people['Year'])
    years = list((years))
    countofpeople = [0]*len(years)
    year_and_countofpeople = dict(zip(years, countofpeople))
    for people in population:
        if (people['Year'] in year_and_countofpeople.keys()
                and people['Region'] in saarccountries):
            year_and_countofpeople[people['Year']
                                   ] += float(people['Population'])

    print(year_and_countofpeople)

    return year_and_countofpeople


def plot(years, population):
    '''for plotting'''

    _, aux = plt.subplots()

    blabels = years

    aux.bar(blabels, population, label=blabels, color='red')
    aux.set_ylabel('Population growth')
    aux.set_title('Saarc population over years')
    # ax.legend(title='Teams')
    plt.show()


populationdata = []
with open("population-estimates_csv.csv", 'r', encoding='utf-8') as file:
    dataofcountries = csv.DictReader(file)
    for details in dataofcountries:
        populationdata.append(details)


year_and_countof_people = calculate(populationdata)
print(year_and_countof_people)
year = year_and_countof_people.keys()
countof_people = year_and_countof_people.values()
plot(year, countof_people)
