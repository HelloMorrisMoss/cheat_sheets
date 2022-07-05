# ## Python ##
# ---------------------------------------------

# datetime.datetime remove timezone
w_tz = datetime.datetime(2022, 5, 19, 9, 14, 32, 0, pytz.UTC)
w_out_tz = w_tz.replace(tzinfo=None)

# to fix jupyter notebook menu and toolbar not showing
!jt -t gruvboxd -T -N -kl

# gives a string of the datetime in isoformat
datetime.datetime.now().isoformat()

# tuple comprehension - doesn't actually exist, the brackets () were taken
    # fastest, but on large enough iterables, mind that it does temporarily require memory for both the list and tuple:
    tuple_var = tuple([i for i in range(10)])
    # possibly 2/3 again longer but doesn't use memory as above:
    tuple_var = tuple(i for i in range(10))
    # there is another option, but it's at best identical to the tuple(generator) above; note the comma
        *(x for x in range(10)),  

# replace every nth instance in a string
def nth_repl_all(s, sub, repl, nth):
    find = s.find(sub)
    # loop util we find no match
    i = 1
    while find != -1:
        # if i  is equal to nth we found nth matches so replace
        if i == nth:
            s = s[:find]+repl+s[find + len(sub):]
            i = 0
        # find + len(sub) + 1 means we start after the last match
        find = s.find(sub, find + len(sub) + 1)
        i += 1
    return s
   
   
# set a variable to a list of the elements in a list (but not the same list, -> new identity)
new_list = original_list[:]
    # example
    l1 = [1, 2, 3]  # original list
    l2 = l1  # these are two variables with the same identity as their value
    l1 is l2  # this is True
    l3 = l1[:]  # l3 now references an "identical" list, but it is not the same list
    l1 is l3  # this is False
    l1[0] = 5  # change a value in the original
    l2[0]  # this is now 5 as well, the value changes "in the other variable", as they are the same list
    l3[0]  # this is still 1 as l3 is not the same list

# restart the current program
os.execl(sys.executable, sys.executable, *sys.argv)
os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)  # works even in there are spaces in filepath
os.execl(sys.executable, f'"{sys.executable}"', *sys.argv)  # works even in there are spaces in filepath, Python 3.6+

# ## pandas ##
# ----------------------------------------------

# rows that contain lists (or other iterable) that aren't empty
df[df['column_name'].map(lambda x: len(x)) > 0]

# do two dataframes contain the same elements; are they "equal"
the_df.equal(the_other_df)

# row with text column that matches...
word = 'substring'
new_df = df[df["col"].str.contains(word)]  # contains
new_df = df[~df["col"].str.contains(word)]  # does not contain
new_df = df[df["col"].str.contains(word, na=False)]  # mixed datatypes

# split a text column on delimiter into...


# filter rows on multiple columns criteria
len_st_mask = df.Length >= mahlo_start_length
len_end_mask = df.Length <= row.mahlo_end_length
both_mask = len_mask & len_end_mask
df[both_mask]

either_mask = len_mask | len_end_mask
df[either_mask]
  

# replace multiple ids in a string for a pandas column referencing another dataframe
https://gist.github.com/HelloMorrisMoss/0cf1a52d49db2d4e95460604d252e4a7

# convert a list of dicts to a single dataframe
pandas.DataFrame([{'time': '13:00', 'value': 5}, {'time': '15:00', 'value': 3}])

# use a column as the index
pandas.DataFrame.set_index('name of column', in_place=True)

# convert multiple pandas.DataFrame columns to numeric (from say strings/'object')
to_numerify_cols = sample_df.columns.drop('non numeric column header')
sample_df[to_numerify_cols] = sample_df[to_numerify_cols].apply(pd.to_numeric, errors='coerce')

# rename pandas columns
# use a dict of {'old_name': 'new_name'}
df = df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'}, in_place=False)
# use a list of headers to replace all of them
df_new = df.set_axis(['a', 'b', 'c', 'd', 'e'], axis=1, inplace=False)
df.columns = ['a', 'b', 'c', 'd', 'e']

# promote the top row of a dataframe to the column headers
df.columns = df.iloc[0]
df = df[1:]

# to drop from a pandas Index, you can pass a list, but not a tuple - as a tuple will be interpreted
#  as a single index (as it's hashable, I believe)
pandas.DataFrame.index.drop(["this", "can't", "be", "a", "tuple"])

# change a pandas column from string-iso format to timestamp
col_name = 't_stamp'
ldf[col_name] = pd.to_datetime(ldf[col_name])

# pop multiple columns from a dataframe to another
df2 = pd.concat([df.pop(x) for x in ['c', 'd']], axis=1)

# add rows from one dataframe to another - if they have the same column names
combined_df = pd.concat([df0, df1])

# rows where a column is in a list
in_rows_df = df[df['A'].isin([3, 6])]

# rows where substring is in column (na=False covers rows that may not have values and are therefor not iterable)
df[df["column_name"].str.contains("substring", na=False)]

# get a single entry series 
df.loc[boolean_results][column_name]

# convert float column to int
df['number column'] = df['number column'].astype(int)

# load columns as certain type
df = pd.read_csv('production_data.csv', header = 0,  dtype = {'work order': str}, engine = 'c')
 
# ## tkinter ##
# ----------------------------------------------
# tkinter window name
root = tk.Tk()
root.title('Hello title bar')

# window size (default is to grow to contain widgets)
root.geometry('800x500')  # width x length

# tkinter variables (StringVar, IntVar) changed event
sv = tkinter.StringVar()
def callback(string_var):
    return string_var.get()  # just the value as a trivial example
sv.trace_add("write", callback)

# get the created/modified time of a file at a path (in seconds since epoch)
os.stat(path_str).st_mtime

# seconds since epoch to datetime
datetime.datetime.fromtimestamp(1234567890)

# horizontal line
self._top_divider = tk.ttk.Separator(self, orient=tk.HORIZONTAL)
self._top_divider.grid(row=30, column=10, columnspan=col_span, sticky='ew', padx=2, pady=2)

# ## sqlalchemy ##
# ----------------------------------------------
# print out the query for viewing, several options
#   add echo=True to the create_engine parameters, will print to logger
engine = create_engine(DATABASE_URI, pool_pre_ping=True, echo=True)

#   print out a specific query
print(str(the_query_obj))

#   print out a specific query and include the parameters (instead of placeholders)
print(str(
    defect_query.statement.compile(compile_kwargs={"literal_binds": True})
    ))

# print out a query that is too long for print/environment
qs = str(defect_query)
while len(qs):
    print(qs[:100])
    qs = qs[100:]

# or a little prettier:
qs = str(defect_query).split(',')
for part in qs:
    if part.startswith(' '):
        part = '\t' + part
    print(part)

# great video on postgres/SQLAlchemy - "Advanced SQL with SQLAlchemy" - Ryan Kelly 
https://www.youtube.com/watch?v=UPoHdCeg0YQ

# ## pip ##
# ----------------------------------------------
# how to install using pip to an offline system
#  on a system with the same platform, python version, and access to pypi.org:
pip download install libary-name  # for individual libraries
pip download install -r requirements.txt  # using a requirements file
# copy the downloaded files to the offline system, then in the environment (eg venv), /download_dir/ should be the
pip install --no-index --find-links /downloaded_dir/ -r requirements.txt  # path to the downloaded file directory

# making xml pretty using python - (xml_raw being xml as a string)
# ------------------------------
# write to a file:
from xml.dom import minidom 
with open('site_list_pretty.xml', 'w') as f:
    f.write(minidom.parseString(xml_raw).toprettyxml(indent='    '))
    
# print to console:
import io
from pprint import pp
from xml.dom import minidom 
with io.StringIO(minidom.parseString(xml_raw).toprettyxml(indent='    ')) as f:  # "pretend" to write it to a file
    pp(f.read())
