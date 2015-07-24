def my_function(times=10):
    test_list = []
    for num in range(times):
        test_list.append( "This is my %i th sentence" % num)
    return test_list
my_list =  my_function()
    
