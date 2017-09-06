import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('movielens/users.dat',sep="::",engine='python',header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movielens/ratings.dat',sep="::", engine='python', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movielens/movies.dat',sep="::", engine='python', header=None, names=rnames)

