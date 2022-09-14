from calculator import square

# if square(2) != 4:   #for testing 
#     print('2 squared was not 4')

# if square(3) != 9:
#     print('3 squared was not 9')

# same as above ^^
# assert means assume, 
def test_square():
    # test_  <must be.  cant change.
    assert square(2) == 4
    assert square(3) == 9

# try:
#     assert square(2) == 4
# except AssertionError:
#     print('square(2) is not 4')

# try:
#     assert square(3) == 9
# except AssertionError:
#     print('square(3) is not 9')

