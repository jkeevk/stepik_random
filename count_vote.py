def vote(votes):
    max_count = 0
    mode = None
    for num in votes:
        count = votes.count(num)
        if count > max_count:
            max_count = count
            mode = num
    print(mode)
	

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))