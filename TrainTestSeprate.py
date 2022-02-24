import shutil, random, os, sys
# mkdir train && mkdir test
folder = '/home/quadro2/PycharmProjects/PyTest/data/MusicSpeech/'
whereto = '/home/quadro2/PycharmProjects/PyTest/data/MusicSpeechTrainTest/'
for d, ds, fs in os.walk(folder):
    for fname in fs:
        if fname[-4:] != '.WAV':
            continue
        if fname[0] == '.':
            continue
        h=d.split('/')
        if random.uniform(0,1) > 0.15:
            if not os.path.exists(whereto + 'train/'+h[-1]+'/'):
                os.makedirs(whereto + 'train/'+h[-1]+'/')
            print (fname, 'to train')
            shutil.copy(d + '/' + fname, whereto + 'train/'+h[-1]+'/')

        else:
            if not os.path.exists(whereto + 'test/'+h[-1]+'/'):
                os.makedirs(whereto + 'test/'+h[-1]+'/')
            print (fname, 'to test')
            shutil.copy(d + '/' + fname, whereto + 'test/'+h[-1]+'/')
