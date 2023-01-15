import csv
import matplotlib.pyplot as plt


def calculate(population):
    '''for calculating'''
    asean_countries = ['Indonesia', 'Malaysia', 'Philippines', 'Singapore',
                       'Thailand', 'Brunei Darussalam',
                       'Viet Nam', "Lao People's Democratic Republic",
                       'Myanmar', 'Cambodia']
    peoplecount = [0]*len(asean_countries)
    aseancountries_peoplecount = dict(zip(asean_countries, peoplecount))
    for people in population:

        if people['Region'] in aseancountries_peoplecount.keys():
            aseancountries_peoplecount[people['Region']
                                       ] += float(people['Population'])

    print(aseancountries_peoplecount)
    return aseancountries_peoplecount


def plot(aseancountries, population):
    '''for plotting'''
    _, aux = plt.subplots()
    blabels = aseancountries
    aux.bar(blabels,    population, label=blabels, color='red')
    aux.set_ylabel('Population')
    aux.set_title(
        'For the year 2014. Bar Chart of population of ASEAN countries')
    # aux.legend(title='Teams')
    plt.show()


populationdata = []
with open("population-estimates_csv.csv", 'r', encoding='utf-8') as file:
    dataofcountries = csv.DictReader(file)
    for details in dataofcountries:
        populationdata.append(details)


aseancountries_people_count = calculate(populationdata)
print(aseancountries_people_count)
Asean_countries = aseancountries_people_count.keys()
people_count = aseancountries_people_count.values()
plot(Asean_countries, people_count)
