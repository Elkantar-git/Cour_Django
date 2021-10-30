txt = open("album.txt",'r')
list = txt.read().split('\n')
txt.close()

artistr = open("return_artist.txt",'w')
albumr = open("return_album.txt",'w')
linkr = open("return_link.txt",'w')

for i in range(0, int(len(list)/4)):
    x = list[i*4:(i+1)*4]

    art = x[1].replace(" ", "").replace("'", "")
    alb = x[2].replace(" ", "").replace("'", "")

    artist = '{} = Artist.objects.create(name="{}")\n'.format(art, x[1])
    album = '{} = Album.objects.create(title="{}", picture="{}", pk={})\n'.format(alb, x[2], x[3], x[0])
    link = '{}.artists.add({})\n'.format(alb, art)


    artistr.write(artist)
    albumr.write(album)
    linkr.write(link)

artistr.close()
albumr.close()
linkr.close()
