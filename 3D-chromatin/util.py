import straw

def oe_norm(hic_file,cl,resolution):
    chrs = [str(i) for i in range(1, 23)] + ['X']
    for chr in chrs:
        print(chr)
        f = open('%s_contact_map/chr%s_%s.txt' % (cl,chr,resolution), 'w')
        result = straw.straw('oe', 'NONE', hic_file, chr, chr,
                             'BP', resolution)
        for i in range(len(result)):
            f.write("{0}\t{1}\t{2}\n".format(result[i].binX, result[i].binY, result[i].counts))
        f.close()



