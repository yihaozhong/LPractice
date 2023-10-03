import csv

class Movie:
    def __init__(self, title, genre, year) -> None:
        self.title = title
        self.genre = genre
        self.year = year

    def __repr__(self) -> str:
        pass

class MovieCatalog:
    # O(N)
    def __init__(self, csv_file) -> None:
        self.movies = []

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title, genre, year = row
                movie = Movie(title, genre, year)

                self.movies.append(movie)

    # O(N)
    def search(self, genre, year_range):
        start, end = year_range

        return [movie for movie in self.movies if movie.genre == genre and movie.year >= start and movie.year <= end]
    

class OptimizedMovieCatelorg:
    def __init__(self, csv_file) -> None:
        self.movies = []

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title, genre, year = row
                movie = Movie(title, genre, year)

                if genre not in self.genre_to_movies:
                    self.genre_to_movies[genre] = []
                self.genre_to_movies[genre].append(movie)
                
                self.year_to_movies[int(year) - 1900].append(movie)
    
    def search(self, genre, year_range):
        start, end = year_range
        matching_movies = []
        # O(k) for the k movie in genre
        for movie in self.genre_to_movies.get(genre, []):
            if start <= movie.release_year <= end:
                matching_movies.append(movie)

        return matching_movies
