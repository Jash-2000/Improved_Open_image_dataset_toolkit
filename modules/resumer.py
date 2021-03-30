import pandas as pd
import glob

def resume(args):

    csv_type_list = []
    limit_list = []

    for i in range(len(args.classes)):
        csv_type_list.append(args.type_csv)
        limit_list.append(args.limit)

    df1 = pd.DataFrame({"class":args.classes, 
                         "type":csv_type_list,
                         "limit":limit_list}) 
    print("\n")
    print(df1)
    print("\n")


    try:
        df = pd.read_csv("log.csv")	
        df.append(df1, ignore_index = True)
    except:
        df1.to_csv("log.csv")
        df = df1
     
    print("\n")
    print(df)
    print("\n")

    classes_list = []
    classes_list.append(df['class'].iloc[0])
    args.classes = classes_list
    args.type_csv = df['type'].iloc[0]
    args.limit = df['limit'].iloc[0]

    df = df.drop([0]).reset_index(drop=True)
    df.to_csv("log.csv")

    print(df)

    return args

def resume_last_state():
    
    filename = 'log.csv'
    # Use this function to search for any files which match your filename
    files_present = glob.glob(filename)

    if not files_present:
        print("The file does not exist. You can not resume the task if you have not started it yet!!!!")
    else:
        df = pd.read_csv("log.csv")	

    for i in range(len(df.columns)): 
        classes_list = []
        classes_list.append(df['class'].iloc[0])
        args.classes = classes_list
        args.type_csv = df['type'].iloc[0]
        args.limit = df['limit'].iloc[0]

        bounding_boxes_images(args, DEFAULT_OID_DIR)

        df = df.drop([0]).reset_index(drop=True)
        df.to_csv("log.csv")

    print(df)

    return args