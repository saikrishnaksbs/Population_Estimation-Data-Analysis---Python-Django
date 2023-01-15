import csv
import matplotlib.pyplot as plt


def calculate(population):
    '''for calculating'''
    years = []
    people_count = []
    for people in population:
        people_count.append(float(people['Population']))
        years.append(int(people['Year']))
    years_and_peoplecount = [years, people_count]
    return years_and_peoplecount


def plot(years, population):
    '''for plotting'''
    _, aux = plt.subplots()

    blabels = years[-50:]

    aux.bar(blabels,    population[-50:], label=blabels, color='red')

    aux.set_ylabel('Population growth ')

    aux.set_title('India population over years - Bar Plot')

    # aux.legend(title='Teams')

    plt.show()


populationdata = []
with open("population-estimates_csv.csv", 'r', encoding='utf-8') as file:
    dataofcountries = csv.DictReader(file)
    for details in dataofcountries:
        populationdata.append(details)


years_and_people_count = calculate(populationdata)
print(years_and_people_count)
years_list = years_and_people_count[0]
peoplecount = years_and_people_count[1]
plot(years_list, peoplecount)
