import straw
import numpy as np
import os
from scipy.sparse import load_npz
def pad_seq_matrix(matrix, pad_len=300):
    # add flanking region to each sample
    paddings = np.zeros((1, 4, pad_len)).astype('int8')
    dmatrix = np.concatenate((paddings, matrix[:, :, -pad_len:]), axis=0)[:-1, :, :]
    umatrix = np.concatenate((matrix[:, :, :pad_len], paddings), axis=0)[1:, :, :]
    return np.concatenate((dmatrix, matrix, umatrix), axis=2)

def pad_signal_matrix(matrix, pad_len=300):
    paddings = np.zeros(pad_len).astype('float32')
    dmatrix = np.vstack((paddings, matrix[:, -pad_len:]))[:-1, :]
    umatrix = np.vstack((matrix[:, :pad_len], paddings))[1:, :]
    return np.hstack((dmatrix, matrix, umatrix))

def load_refgenome():
    ref_genome={}
    ref_path='/scratch/drjieliu_root/drjieliu/zhenhaoz/ref_genome/'
    chrs=[str(i) for i in range(1,23)]+['X']
    for chr in chrs:
        ref_file = os.path.join(ref_path, 'chr%s.npz' % chr)
        ref_gen_data = load_npz(ref_file).toarray().reshape(4, -1, 1000).swapaxes(0, 1)
        print(chr, ref_gen_data.shape)
        ref_genome[chr]=pad_seq_matrix(ref_gen_data)
    return ref_genome


def process_train_data():
    resolution = 5000
    chr_lens = [248956422, 242193529, 198295559, 190214555, 181538259, 170805979, 159345973,
                145138636, 138394717, 133797422, 135086622, 133275309, 114364328, 107043718,
                101991189, 90338345, 83257441, 80373285, 58617616, 64444167, 46709983, 50818468, 156040895]
    genome_lens = np.array(chr_lens) // resolution
    chrs = [str(i) for i in range(1, 23)] + ['X']

    input_regions = {}
    for i in range(len(chrs)):
        inputs=[]
        genome_seq=ref_genome[chrs[i]]
        print(genome_seq.shape)
        for bin_idx in np.arange(0,genome_lens[i],50):
            wstart=bin_idx
            wend=wstart+1000
            if genome_seq[wstart:wend].sum() ==1000*1600:
                inputs.append(np.array([wstart,wstart+1000]))

        input_data[chrs[i]]=np.stack(inputs)
        print(genome_lens[i],input_data[chrs[i]].shape)
    with open('/nfs/turbo/umms-drjieliu/usr/zzh/KGbert/chrom_organization/data/input_1Mb_test.pickle','wb') as f:
        pickle.dump(input_data,f)


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


if __name__=='__main__':
    oe_norm(hic_file,cl,resolution)
