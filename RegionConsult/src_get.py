import os
import sys


from __init__ import *


def main(SRC_DIR, fname):
    # Открываем источник, возвращаем в df формате
    def src_xlsx_get(fname):
        for filename in os.listdir(SRC_DIR):
            f = os.path.join(SRC_DIR, filename)
            if os.path.isfile(f):
                if re.findall(re.escape(fname), f):
                    fname = f  
        try:
            return pd.read_csv(fname, encoding='utf-8', delimiter=';')
        except UnicodeDecodeError:
            return pd.read_csv(fname, encoding='windows-1251', delimiter=';')

    source_get = src_xlsx_get(fname)
    return source_get
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
