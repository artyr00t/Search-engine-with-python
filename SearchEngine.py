from google import search

def Search():
    file = open("sites_to_search.txt", "r")
    file2 = open("already_searched_sites.txt", "w")
    documentcontet = file.readlines()
    number_of_content = len(documentcontet)
    loop = 0
    siteslist = []
    loop2 = 0
    for i in range(0, number_of_content):
        for url in search(documentcontet[loop], stop=1):
            siteslist.append(url)
            file2.write(siteslist[loop2]+"\n")
            loop2+= 1
        loop+=1
    file.close()
    file2.close()
if __name__ == '__main__':
    Search()
