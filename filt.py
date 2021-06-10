import pandas as pd
import record


def ph(name):
    file = f'{record.data_path}/{name}.csv'
    return file
    pass


name_list = ['ordinary user', 'blue-1', 'blue-2', 'blue-3', 'orange gold-1', 'orange gold-2', 'orange gold-3']
path_list = []
for j in range(len(name_list)):
    path_list.append(ph(name=f'{name_list[j]}'))
txt_path = record.User_path.csv_txt()
txt_f = open(txt_path, "a+")
for j in range(len(path_list)):
    df = pd.read_csv(path_list[j], encoding='gb18030', lineterminator='\n')
    df_new = df.drop_duplicates(subset=['全文内容'])  # 去重

    df_new = df_new.sort_values(by=['MD5-作者ID', '发布日期']).reset_index(drop=True)
    df_id = df_new.drop_duplicates(subset=['MD5-作者ID'])
    id_l = len(df_id)
    date0 = df_new['发布日期'][0][:].split(' ')[0]
    i = 0
    k = 0
    _ = 0
    id_drop = []
    while _ < len(df_new):  # 列出日发帖>50的机器人的作者ID值列表
        date = df_new['发布日期'][_][:].split(' ')[0]
        if date == date0:
            i += 1
        else:
            date0 = df_new['发布日期'][_][:].split(' ')[0]
            i = 0
        id = df_new['MD5-作者ID'][_]
        id1 = df_id['MD5-作者ID'].values[k]
        if i > 50:  # 超50条
            if id == id1:
                id_drop.append(id)
                if k < id_l - 1:
                    k += 1
                    _ = df_id['MD5-作者ID'].index[k]
                    date0 = df_new['发布日期'][_][:].split(' ')[0]
                    i = 0
                    _ -= 1
            else:
                print('{},MD5-作者ID error,{},{}'.format(_, id, id1))
        else:
            if k < id_l - 1:
                if id != id1:
                    k += 1
        _ += 1
        pass
    df_drop = df_new[~df_new['MD5-作者ID'].isin(id_drop)].reset_index(drop=True)  # 去除机器人:每日发帖超过50条
    id_filt = len(df_drop.drop_duplicates(subset=['MD5-作者ID'])) - 1
    txt_f.write(f'\n{name_list[j]}.csv, all_id:{id_l-1}, drop_id:{len(id_drop)}, filt_id:{id_filt}, '
                f'source:{len(df)}, {len(df_new)}, end:{len(df_drop)}')
    df_drop.to_csv(f'{record.local_path}/_csv/{name_list[j]}_d.csv', encoding='gb18030', index=False)
txt_f.close()
