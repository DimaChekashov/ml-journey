def main():
    users = input().split() 
    movies = input().split()

    for u in range(len(users)):
        parts = input().split()
        user = parts[0]
        count = int(parts[1])
        watched = parts[2:]

        if count != len(movies):
            return "NO"

        for movie in movies:
            if movie not in watched:
                return "NO"
    
    return "YES"


if __name__ == '__main__':
    print(main())
