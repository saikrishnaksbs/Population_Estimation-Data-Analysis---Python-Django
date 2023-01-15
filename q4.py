import csv
import matplotlib.pyplot as plt


def calculate(populationdata):
    '''for calculating'''
    years = list(range(2004, 2015))
    print(years)
    aseancountries = ['Indonesia', 'Malaysia', 'Philippines',
                      'Singapore', 'Thailand',
                      'Brunei Darussalam', 'Viet Nam',
                      "Lao People's Democratic Republic",
                      'Myanmar', 'Cambodia']
    population = []
    years_and_aseancountries = {}

    for population in populationdata:

        year = int(population["Year"])
        country = population["Region"]
        popu_count = float(population['Population'])

        if country in aseancountries and year in years:
            if year not in years_and_aseancountries:
                years_and_aseancountries[year] = {}
                if country not in years_and_aseancountries[year]:
                    years_and_aseancountries[year][country] = popu_count
                else:
                    years_and_aseancountries[year][country] += popu_count
            else:
                if country not in years_and_aseancountries[year]:
                    years_and_aseancountries[year][country] = popu_count
                else:
                    years_and_aseancountries[year][country] += popu_count

    return years_and_aseancountries


def plot(years, asean_countries_population):
    '''for plotting'''
    bar_width = 0.1
    population_for_plotting = [[]]*10
    print(population_for_plotting)
    aseancountries = ['Indonesia', 'Malaysia', 'Philippines',
                      'Singapore', 'Thailand',
                      'Brunei Darussalam', 'Viet Nam',
                      "Lao People's Democratic Republic",
                      'Myanmar', 'Cambodia']
    colors = ['blue', 'black', 'green', 'yellow',
              'red', 'pink', 'orange', 'cyan', 'grey', 'lime']
    for i in range(10):
        if i == 0:
            population_for_plotting[i] = years
        else:
            population_for_plotting[i] = [j+bar_width for j in
                                          population_for_plotting[i-1]]

    plt.figure(figsize=(20, 5))
    for k in range(10):
        plt.bar(population_for_plotting[k],
                asean_countries_population[k],
                width=bar_width, label=aseancountries[k], color=colors[k])

    plt.xticks(population_for_plotting[0], years)
    plt.legend()
    plt.show()


def tranform(asean_population):
    '''to transform'''
    count_per_year = list(asean_population.values())
    population_count = []
    for year in range(11):
        count = list(count_per_year[year].values())
        population_count.append(count)

    print(population_count)
    transformed_asean_population = list(map(list, zip(*population_count)))

    return transformed_asean_population


population_data = []

with open("population-estimates_csv.csv", 'r', encoding='utf-8') as file:
    dataofcountries = csv.DictReader(file)
    for details_of_population in dataofcountries:
        population_data.append(details_of_population)


Aseancountriespopulation = calculate(population_data)
print(Aseancountriespopulation.keys())
transformed_asian_list = tranform(Aseancountriespopulation)
print(list(Aseancountriespopulation.keys()))
print(transformed_asian_list)
plot(list(Aseancountriespopulation.keys()), transformed_asian_list)
