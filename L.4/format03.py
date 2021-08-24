print(' {0:8} |     {1:8} ' .format('fruit','Quantity'))
print(' {0:8} |     {1:8} ' .format('Apple','3'))
print(' {0:8} |     {1:8} ' .format('Orange','10'))
print('-' * 50)
#> right
print(' {0:8} |     {1:>8} ' .format('fruit','Quantity'))
print(' {0:8} |     {1:>8} ' .format('Apple','3'))
print(' {0:8} |     {1:>8} ' .format('Orange','10'))

print('-' * 50)
#< left
print(' {0:8} |     {1:<8} ' .format('fruit','Quantity'))
print(' {0:8} |     {1:<8} ' .format('Apple','3'))
print(' {0:8} |     {1:<8} ' .format('Orange','10'))

print('-' * 50)
#^ center
print(' {0:8} |     {1:^8} ' .format('fruit','Quantity'))
print(' {0:8} |     {1:^8} ' .format('Apple','3'))
print(' {0:8} |     {1:^8} ' .format('Orange','10'))

print('-' * 50)
#.2f
print(' {0:8} |     {1:<8.2f} ' .format('fruit','Quantity'))
print(' {0:8} |     {1:<8.2f} ' .format('Apple','3'))
print(' {0:8} |     {1:<8.2f} ' .format('Orange','10'))