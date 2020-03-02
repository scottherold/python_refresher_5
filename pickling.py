import pickle

# data
imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhmen'),
           (4, 'Kentish Town Waltz')))

# writes to binary/pickle file
# .pickle is an extension only recognized by Python
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

# .pickle'd information can easily be retired with a .load() method
with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

# unpack
album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)