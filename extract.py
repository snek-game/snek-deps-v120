import sys, os, fnmatch, zipfile, multiprocessing

EXEC_DIR = os.path.abspath(os.path.dirname(__file__))

def extract_zip(file_path):
  with zipfile.ZipFile(file_path, 'r') as z:
    z.extractall(os.path.dirname(file_path))
    print 'Extracted', os.path.relpath(file_path, EXEC_DIR)

if __name__ == '__main__':
  
  sys.path.append(os.path.abspath(os.path.join(EXEC_DIR, '..', '..', 'tools', 'pytools')))

  from joblib import Parallel, delayed

  os.chdir(EXEC_DIR)

  matches = []
  for folder in ['bin', 'lib']:
    for root, dirnames, filenames in os.walk(folder):
      for filename in fnmatch.filter(filenames, '*.zip'):
        matches.append(os.path.join(root, filename))

  Parallel(n_jobs=multiprocessing.cpu_count())(delayed(extract_zip)(f) for f in matches)