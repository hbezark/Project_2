## SI 206 W17 - Project 2

## COMMENT HERE WITH:
## Your name: Hana Bezark
## Anyone you worked with on this project: Emma Welch

## Below we have provided import statements, comments to separate out the 
#parts of the project, instructions/hints/examples, and at the end, TESTS.

###########

## Import statements
import unittest
import requests
import re
from bs4 import BeautifulSoup


## Part 1 -- Define your find_urls function here.
## INPUT: any string
## RETURN VALUE: a list of strings that represents all of the URLs in the input string


## For example: 
## find_urls("http://www.google.com is a great site") should return ["http://www.google.com"]
## find_urls("I love looking at websites like http://etsy.com and http://instagram.com and stuff") should return ["http://etsy.com","http://instagram.com"]
## find_urls("the internet is awesome #worldwideweb") should return [], empty list

def find_urls(s):
    return re.findall('http[^\s]?://.?[^\s]+\..?[^\s]+', s)



## PART 2  - Define a function grab_headlines.
## INPUT: N/A. No input.
## Grab the headlines from the "Most Read" section of 
## http://www.michigandaily.com/section/opinion

def grab_headlines():
    headlines = []
    r = requests.get("http://www.michigandaily.com/section/opinion")
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find('div', class_ = 'panel-pane pane-mostread')
    list_ = div.find_all('li')
    for item in list_:
        headlines.append(item.find('a').contents[0])
    return (headlines)



## PART 3 (a) Define a function called get_umsi_data.  It should create a dictionary
## saved in a variable umsi_titles whose keys are UMSI people's names, and whose 
## associated values are those people's titles, e.g. "PhD student" or "Associate 
## Professor of Information"...
## Start with this page: https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All  
## End with this page: https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page=12 
## INPUT: N/A. No input.
## OUTPUT: Return umsi_titles
## Reminder: you'll need to use the special header for a request to the UMSI site, like so:
## requests.get(base_url, headers={'User-Agent': 'SI_CLASS'}) 

def get_umsi_data():
    umsi_titles = {}
    name_lst = []
    
    base_url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All"
    
    for num in range(0,12):
        new_url = base_url + '&page=%s' %str(num)

        r = requests.get(new_url, headers = {'User-Agent': 'SI_CLASS'})
        soup = BeautifulSoup(r.text, 'html.parser')
        for h in soup.find_all(class_ = "ds-1col node node-person node-teaser view-mode-teaser clearfix"):
            for x in h.find_all(class_ = "field-item even", property="d:title"):
                name_lst.append((x.text))
        title_lst = []
        for a in soup.find_all(class_ = "field field-name-field-person-titles field-type-text field-label-hidden"):
            for b in a.find_all(class_ = "field-item even"):
                title_lst.append((b.text))
    combo = zip(name_lst, title_lst)
    umsi_titles = dict(combo)
    return (umsi_titles)
           

## PART 3 (b) Define a function called num_students.  
## INPUT: The dictionary from get_umsi_data().
## OUTPUT: Return number of PhD students in the data.  (Don't forget, I may change the input data)
def num_students(data):
    y = sum(x == "PhD student" for x in data.values())
    print (y)
    #PhD = 0
    #for person in data:
        #if 'PhD' in data[person]:
            #PhD += 1
    #return PhD 

    #PhD = 0
    #for value in data.values():
        #if data[value] == 'PhD student':
            #PhD += 1
    #return PhD

########### TESTS; DO NOT CHANGE ANY CODE BELOW THIS LINE! ###########
def test(got, expected, pts):
    score = 0;
    if got == expected:
        score = pts
        print(" OK ",end=" ")
    else:
        print (" XX ", end=" ")
    print("Got: ",got, "Expected: ",expected)

    return score


def main():
    total = 0
    print()
    print ('Task 1: Find URLS')
    total += test(find_urls("http://www.google.com is a great site"),["http://www.google.com"],10)
    total += test(find_urls("I love looking at websites like http://etsy.com and http://instagram.com and lol.com and stuff"),["http://etsy.com","http://instagram.com"],10)
    total += test(find_urls("I love looking at websites like http://etsy and http://instagram.com and https://www.bbc.co.uk and stuff"),["http://instagram.com","https://www.bbc.co.uk"],10)
    total += test(find_urls("the internet is awesome #worldwideweb"),[],10)
    total += test(find_urls("http://.c"),[],10)


    print('\n\nTask 2: Michigan Daily')
    total += test(grab_headlines(),["MSW students protest staff member's email based on religious bias", 'Teen arrested at Blake Transit Center', "Racist flyers calling to 'Make America White Again' found near Stockwell", "Protesters take to LSA SG panel on C.C. Little's renaming", 'Michigan football player Nate Johnson arrested for domestic violence'],50)


    print('\n\nTask 3: UMSI Directory')

    data = get_umsi_data()
   
    total += test(data,{'Mohamed Abbadi': 'PhD student', 'Mark Ackerman': 'George Herbert Mead Collegiate Professor of Human-Computer Interaction, Professor of Information, School of Information, Professor of Electrical Engineering and Computer Science, College of Engineering and Professor of Learning Health Sciences, Medical Sc', 'Eytan Adar': 'Associate Professor of Electrical Engineering and Computer Science, College of Engineering and Associate Professor of Information, School of Information', 'Julia Adler-Milstein': 'Associate Professor of Information, School of Information and Associate Professor of Health Management and Policy, School of Public Health', 'Wei Ai': 'PhD student', 'Rasha Alahmad': 'PhD student', 'Tawfiq Ammari': 'PhD student', 'Marsha Antal': 'School Registrar', 'Deborah Apsley': 'Director of Human Resources and Support Services', 'Sarah Argiero': 'Assistant Director, Master of Science in Information Program', 'Daniel Atkins III': 'Professor Emeritus of Information, School of Information and Professor Emeritus of Electrical Engineering and Computer Science, College of Engineering', 'Seyram Avle': 'Research Investigator, Information and Research Fellow, School of Information', 'Todd Ayotte': 'Director of Finance', 'Alicia Baker': 'Administrative Assistant', 'Reginald Beasley': 'Admissions and Student Affairs Assistant', 'Vadim Besprozvany': 'Lecturer III in Information, School of Information', 'Lindsay Blackwell': 'PhD student', 'Francis Blouin Jr': 'Professor of Information, School of Information and Professor of History, College of Literature, Science, and the Arts', 'Walt Borland': 'Adjunct Clinical Associate Professor of Information, School of Information', 'Lia Bozarth': 'PhD student', 'Leah Brand': 'Project Manager', 'Stephanie Brenton': 'Intermittent Lecturer in Information, School of Information', 'Robin Brewer': 'Assistant Professor/Postdoctoral/President Fellow, School of Information', 'Christopher Brooks': 'Research Assistant Professor, School of Information', 'Sophia Brueckner': 'Assistant Professor of Art and Design, Penny W Stamps School of Art and Design and Assistant Professor of Information, School of Information', 'Ceren Budak': 'Assistant Professor of Information, School of Information and Assistant Professor of Electrical Engineering and Computer Science, College of Engineering', 'Lorraine Buis': 'Assistant Professor of Family Medicine, Medical School and Assistant Professor of Information, School of Information', 'Glenda Bullock': 'Associate Director of Communications', 'Ryan Burton': 'PhD student', 'Ayse Buyuktur': 'Research Area Specialist, School of Information', 'Stacy Callahan': 'Financial Specialist Senior', 'Dan Cameron': 'Global Engagement Coordinator', 'Nick Campbell': 'Assistant Director of Development', 'Samuel Carton': 'PhD student', 'Kayla Carucci': 'PhD student', 'Melissa Chalmers': 'PhD student', 'Priyank Chandra': 'PhD student', 'Daphne Chang': 'PhD student', 'Yan Chen': 'PhD student', 'Jacques Chestnut': ' ', 'Padma Chirumamilla': 'PhD student', 'Heeryung Choi': 'PhD student', 'Amanda Ciacelli': 'Research and HR Administrative Assistant', 'Jaclyn Cohen': 'Lecturer III in Information, School of Information', 'Alain Cohn': 'Assistant Professor of Information, School of Information', 'Kevyn Collins-Thompson': 'Associate Professor of Information, School of Information and Associate Professor of Electrical Engineering and Computer Science, College of Engineering', 'Paul Conway': 'Associate Professor of Information, School of Information', 'Paul Courant': 'Harold T Shapiro Collegiate Professor of Public Policy, Arthur F Thurnau Professor, Senior Counselor to the Provost, Office of the Provost and Executive Vice President for Academic Affairs, Presidential Bicentennial Professor, Professor of Public Policy, ', 'Andrea Daly': 'Associate Director of Development and Alumni Relations', 'Shevon Desai': 'Senior Associate Librarian, Graduate Library, University Library', 'Tawanna Dillahunt': 'Assistant Professor of Information, School of Information and Assistant Professor of Electrical Engineering and Computer Science, College of Engineering', 'Nia Dowell': 'Research Investigator, Information and Research Fellow, School of Information', 'James Duderstadt': 'President Emeritus and University Professor of Science and Engineering', 'Katie Dunn': 'Assistant Director of Career Development and Adjunct Lecturer in Information, School of Information', 'Joan Durrance': 'Professor Emerita of Information, School of Information', 'Paul Edwards': 'Professor of Information, School of Information and Professor of History, College of Literature, Science, and the Arts', 'Laura Elgas': 'Director of Admissions and Student Affairs', 'Nicole Ellison': 'Professor of Information, School of Information', 'Rebecca Epstein': 'Executive Secretary', 'Luis Escareno': 'Development and Alumni Relations Generalist', 'Veronica Falandino': 'Associate Director for Admissions and Student Affairs', 'Thomas Finholt': 'Dean and Professor of Information, School of Information', 'Barry Fishman': 'Arthur F Thurnau Professor, Professor of Education, School of Education and Professor of Information, School of Information', 'Kanda Fletcher': 'Administrative Assistant Senior', 'Allen Flynn': 'PhD student', 'Kristin Fontichiaro': 'Clinical Associate Professor of  Information, School of Information', 'Rebecca Frank': 'PhD student', 'Charles Friedman': 'Josiah Macy, Jr Professor of Medical Education, Chair, Department of Learning Health Sciences, Professor of Learning Health Sciences, Medical School, Professor of Information, School of Information and Professor of Health Management and Policy, School of ', 'Carolyn Frost': 'Professor Emerita of Information, School of Information', 'George Furnas': 'Professor of Information, School of Information, Professor of Electrical Engineering and Computer Science, College of Engineering and Prof of Psychology, College of Literature, Science and the Arts', 'Patricia Garcia': 'Assistant Professor of Information, Research Fellow, Information, Research Investigator, Information, School of Information', 'Eric Gilbert': 'John Derby Evans Endowed Professor of Information and Associate Professor of Information, School of Information', 'Elena Godin': 'Lecturer III in Information, School of Information', 'Iris Gomez-Lopez': 'Research Fellow, Information, School of Information', 'Carolyn Gregurich': 'HR Generalist', 'Tamy Guberek': 'PhD student', 'Hannah Haley': ' ', 'Brian Hall': 'PhD student', 'Alexandra Haller': ' ', 'David Hanauer': 'Associate Professor of  Pediatrics and Communicable Diseases, Medical School and Clinical Associate Professor of Information, School of Information', 'Edward Happ': 'Lecturer IV in Information and Research Investigator, School of Information', 'Jean Hardy': 'PhD student', 'Carl Haynes': 'PhD student', 'Shiqing (Licia) He': 'PhD student', 'Margaret Hedstrom': 'Robert M Warner Collegiate Professor of Information, Professor of Information, School of Information and Faculty Associate, Institute for Social Research', 'Libby Hemphill': 'Associate Professor of Information, School of Information and Research Associate Professor, Inter-University Consortium for Political and Social Research, Institute for Social Research', 'Michael Hess': 'Solution Architect Lead and Adjunct Lecturer in Information, Sch of Information, Director of Infrastructure ActiveStep, App Programmer/Analyst Ld, Family Medicine, Medical School', 'David Hessler': 'Professor Emeritus of Information, School of Information', 'James Hilton': 'Arthur F Thurnau Professor, Vice Provost for Academic Innovation, Office of the Provost and Executive Vice President for Academic Affairs, Dean of Libraries, University Library, Professor of Information, School of Information and Faculty Associate, Resear', 'Erik Hofer': 'Chief Information Officer and Clinical Assistant Professor of Information, School of Information', 'Lija Hogan': 'Intermittent Lecturer in Information, School of Information', 'Maurita Holland': 'Associate Professor Emerita of Information, School of Information', 'Caitlin Holman': 'PhD student', 'Evan Hoye': ' ', 'Joey Hsiao': 'PhD student', 'Chuan-Che Huang': 'PhD student', 'Julie Hui': 'Research Fellow, School of Information', 'Graham Hukill': 'Intermittent Lecturer in Information, School of Information', 'Pei-Yao Hung': 'PhD student', 'Linh Huynh': 'Academic Advisor', 'Bradley Iott': 'PhD student', 'Kelly Iott': 'Facilities Coordinator', 'Sheryl James': 'Public Relations Specialist', 'Grace YoungJoo Jeon': 'Research Fellow, Information, School of Information', 'Craig Johnson': 'Web Software Developer', 'Lynn Johnson': 'Professor of Dentistry, Department of Periodontics and Oral Medicine, Associate Dean for Faculty Affairs and Institutional Effectiveness, School of Dentistry and Clinical Professor of Information, School of Information', 'Ju Yeon Jung': 'PhD student', 'David Jurgens': 'Assistant Professor of Information, School of Information', 'Vaishnav Kameswaran': 'PhD student', 'Tsuyoshi Kano': 'PhD student', 'Harmanpreet Kaur': 'PhD student', 'Matthew Kay': 'Assistant Professor of Information, School of Information and Assistant Professor of Electrical Engineering and Computer Science, College of Engineering', 'Elizabeth Kaziunas': 'PhD student', 'Devon Keen': 'Assistant Director for Outreach and External Transfers', 'Sangmi Kim': 'PhD student', 'John Leslie King': 'William Warner Bishop Collegiate Professor of Information and Professor of Information, School of Information', 'Predrag Klasnja': 'Assistant Professor of Information, School of Information and Assistant Professor of Health Behavior and Health Education, School of Public Health', 'Daniel Klyn': 'Intermittent Lecturer I in Information, School of Information', 'Annie Knill': 'Assistant Director, Health Informatics Program', 'Kelly Kowatch': 'Director of Engaged Learning Programs and Adjunct Lecturer in Information, School of Information', 'Joanna Kroll': 'Director of Career Development', 'Erin Krupka': 'Associate Professor of Information, School of Information', 'Carl Lagoze': 'Associate Professor of Information, School of Information', 'Clifford Lampe': 'Associate Professor of Information, School of Information', 'Walter Lasecki': 'Assistant Professor of Electrical Engineering and Computer Science, College of Engineering and Assistant Professor of Information, School of Information', 'Anna Lawrence': 'Digital Content Strategist', 'Katherine Lawrence': 'Research Area Specialist Lead and Research Investigator, School of Information', 'Judy Lawson': 'Assistant Dean for Diversity, Equity, and Inclusion', 'Claudia Leo': 'Programming and Media Coordinator', 'Margaret Levenstein': 'Adjunct Professor of Business Economics and Public Policy, Stephen M Ross School of Business, Research Professor, Survey Research Center, ISR Center Director, Institute for Social Research and Research Professor, School of Information', 'Melissa Levine': 'Librarian, Library Research - Copyright, University Library', 'Linfeng Li': 'PhD student', 'Yingzhi Liang': 'PhD student', 'cindy lin': 'PhD student', 'Silvia Lindtner': 'Assistant Professor of Information, School of Information and Assistant Professor of Art and Design, Penny W Stamps School of Art and Design', 'Jessica Litman': 'John F Nickoll Professor of Law, Professor of Law, Law School and Professor of Information, School of Information', 'John Lockard': 'Unix and IT Security Administrator', 'Jiaqi Ma': 'PhD student', 'Jeffrey MacKie-Mason': 'Dean Emeritus, Arthur W Burks Collegiate Professor Emeritus of Information and Computer Science, Professor Emeritus of Information, School of Information, Professor Emeritus of Economics, College of Literature, Science, and the Arts and Professor Emeritus', 'Danaja Maldeniya': 'PhD student', 'Megh Marathe': 'PhD student', 'Karen Markey': 'Professor of Information, School of Information', 'Robert Markum': 'PhD student', 'Allan Martell': 'PhD student', 'Yusuf Masatlioglu': 'Visiting Associate Professor of Economics, College of Literature, Science, and the Arts and Adjunct Associate Professor of Information, School of Information', 'Tonya McCarley': 'Intermittent Lecturer in Information, School of Information', 'Aprille McKay': 'Associate Archivist, Bentley Historical Library and Assistant Director, Bentley Historical Library and Adjunct Lecturer in Information, School of Information', 'Qiaozhu Mei': 'Associate Professor of Information, School of Information and Associate Professor of Electrical Engineering and Computer Science, College of Engineering', 'Abraham Mhaidli': 'PhD student', 'Markus Mobius': 'Adjunct Associate Professor of Information, School of Information', 'Liz Morris': 'PhD student', 'Carol Moser': 'PhD student', 'Nayiri Mullinix': 'Community Engagement and Exchange Coordinator', 'Sungjin Nam': 'PhD student', 'Michael Nebeling': 'Assistant Professor of Information, School of Information and Assistant Professor of Electrical Engineering and Computer Science, College of Engineering', 'Heather Newman': 'Director of Marketing and Communications', 'Mark Newman': 'Associate Professor of Information, School of Information and Associate Professor of Electrical Engineering and Computer Science, College of Engineering', 'Paige Nong': 'Program Manager and Research Coordinator', 'Adrienne Nwachukwu': 'Marketing Project Manager', "Rebecca O'Brien": 'Director of Research Administration', "Alaina O'Connor": 'Social Media Specialist', "Sile O'Modhrain": 'Associate Professor of Music, School of Music, Theatre & Dance and Associate Professor of Information, School of Information', 'Jo Angela Oehrli': 'Senior Associate Librarian, Learning and Teaching, University Library and Adjunct Lecturer in Curriculum Support, College of Literature, Science, and the Arts', 'Ihudiya Ogbonnaya-Ogburu': 'PhD student', 'Gary Olson': 'Professor Emeritus of Information, School of Information and Professor Emeritus of Psychology, College of Literature, Science, and the Arts', 'Judith Olson': 'Professor Emerita of Information, School of Information, Professor Emerita of Computation and Information Systems, Stephen M Ross School of Business and Professor Emerita of Psychology, College of Literature, Science, and the Arts', 'Steve Oney': 'Assistant Professor of Information, School of Information and Assistant Professor of Electrical Engineering and Computer Science, College of Engineering', 'Rebecca Pagels': 'Executive Director of Development and Alumni Relations', 'Joyojeet Pal': 'Assistant Professor of Information, School of Information', 'Sun Young Park': 'Assistant Professor of Art and Design, Penny W Stamps School of Art and Design and Assistant Professor of Information, School of Information', 'Dale Parry': 'Associate Director of Marketing', 'Gaurav Paruthi': 'PhD student', 'Desmond Patton': 'Assistant Professor of Social Work, School of Social Work and Assistant Professor of Information, School of Information', 'Hao Peng': 'PhD student', 'Kathryn Peters': 'Assistant Director for Undergraduate Programs', 'Chanda Phelan': 'PhD student', 'Casey Pierce': 'Assistant Professor of Information, School of Information', 'Edward Platt': 'PhD student', 'Martha Pollack': 'Professor of Information, School of Information, Professor of Electrical Engineering and Computer Science, College of Engineering and Provost and Executive Vice President for Academic Affairs, Office of the Provost and Executive Vice President for Academi', 'Corey Powell': 'Statistician Lead and Leo Adjunct Lecturer, School of Information', 'Christopher Quarles': 'PhD student', 'Dragomir Radev': 'Adjunct Professor of Information, School of Information and Adjunct Professor of Electrical Engineering and Computer Science, College of Engineering', 'Sonia Raheja': 'Marketing Assistant Associate', 'Shriti Raj': 'PhD student', 'Ashwin Rajadesingan': 'PhD student', 'Paul Resnick': 'Michael D Cohen Collegiate Professor of Information, Associate Dean for Research and Faculty Affairs, Professor of Information and Interim Director of Health Informatics, School of Information', 'Soo Young Rieh': 'Associate Professor of Information, School of Information', 'Lionel Robert': 'Associate Professor of Information, School of Information', 'Catherine Robinson': 'Research Process Coordinator', 'Daniel Romero': 'Assistant Professor of Information, School of Information, Assistant Professor of Electrical Engineering and Computer Science, College of Engineering and Assistant Professor of Complex Systems, College of Literature, Science, and the Arts', 'Victor Rosenberg': 'Associate Professor Emeritus of Information, School of Information', 'Tanya Rosenblat': 'Associate Professor of Information, School of Information and Associate Professor of Economics, College of Literature, Science, and the Arts', 'Nickie Rowsey': 'Accountant Senior', 'Jumanah Saadeh': 'Student Services Assistant', 'Perry Samson': 'Arthur F Thurnau Professor, Professor of Climate and Space Sciences and Engineering, College of Engineering and Professor of Information, School of Information', 'Nicholas Sands': 'Intermittent Lecturer in Information, School of Information', 'Christian Sandvig': 'Professor of Information, School of Information, Faculty Associate, Center for Political Studies, Institute for Social Research and Professor of Communication Studies, College of Literature, Science, and the Arts', 'Florian Schaub': 'Assistant Professor of Information, School of Information and Assistant Professor of Electrical Engineering and Computer Science, College of Engineering', 'Charles Severance': 'Clinical Associate Professor of Information, School of Information', 'Michael Shallcross': 'Associate Archivist and Assistant Director, Bentley Historical Library and Adjunct Lecturer in Information, School of Information', 'Timothy Shannon': 'MHI Recruiting and Admissions Coordinator', 'Karandeep Singh': 'Assistant Professor of Learning Health Sciences, Medical School', 'Heidi Skrzypek': 'Assistant Director of Human Resources and Support Services', 'Thomas Slavens': 'Professor Emeritus of Information, School of Information', 'Barbara Smith': 'Senior Assistant to the Dean', 'Jeffrey Smith': 'Videographer', 'Elliot Soloway': 'Arthur F Thurnau Professor, Professor of Electrical Engineering and Computer Science, College of Engineering, Professor of Education, School of Education and Professor of Information, School of Information', 'Zhewei Song': 'PhD student', 'Maximilian Speicher': 'Research Fellow, School of Information', 'George Sprague': 'Academic Programs Coordinator', 'Scott Staelgraeve': 'Administrative Director', 'Todd Stuart': 'Events Manager', 'Hariharan Subramonyam': 'PhD student', 'Kyle Swanson': ' ', 'Allison Sweet': 'Graduate Programs Coordinator', 'Rohail Syed': 'PhD student', 'Alissa Talley-Pixley': 'Career Development and Engaged Learning Coordinator', 'Gregory Tasker': ' ', 'Marissa Taylor': 'Business Systems Analyst Intermediate/Associate', 'Stephanie Teasley': 'Research Professor, School of Information', 'D Scott TenBrink': 'Citizen Experience Design Community Development Liaison and Adjunct Lecturer in Information, School of Information', 'Chris Teplovs': 'Lead Developer, Digital Innovation Greenhouse and  Lecturer III in Information, School of Information', 'Andrea Thomer': 'Assistant Professor of Information, School of Information', 'Mark Thompson-Kolar': 'Intermittent Lecturer in Information, School of Information', 'Kentaro Toyama': 'W K Kellogg Professor of Community Information and Associate Professor of Information, School of Information', 'Penny Trieu': 'PhD student', 'Allison Tyler': 'PhD student', 'Douglas Van Houweling': 'Professor of Information, School of Information', 'Colleen Van Lent': 'Lecturer IV in Information, School of Information', 'Tiffany Veinot': 'Associate Professor of Information, School of Information and Associate Professor of Health Behavior and Health Education, School of Public Health', 'VG Vinod Vydiswaran': 'Assistant Professor of Learning Health Sciences, Medical School and Assistant Professor of Information, School of Information', 'David Wallace': 'Clinical Associate Professor of Information, School of Information', 'Lily Wang': ' ', 'Earnest Wheeler': 'PhD student', 'Brooke White': ' ', 'Elizabeth Whittaker': 'PhD student', 'Rachael Wiener': 'Assistant Director of Recruiting and Admissions, School of Information and Intermittent Lecturer in Social Work, School of Social Work', 'Michael Williams': 'Employer Relations Coordinator', 'Andy Wright': 'Systems Programmer Analyst', 'Elizabeth Yakel': 'Senior Associate Dean for Academic Affairs and Professor of Information, School of Information', 'Shiyan Yan': 'PhD student', 'Sarita Yardi Schoenebeck': 'Assistant Professor of Information, School of Information', 'Teng Ye': 'PhD student', 'Iman Yeckehzaare': 'PhD student', 'Jeremy York': 'PhD student', 'David Young': 'Multimedia Designer', 'T Charles Yun': 'Associate Director UMSI Computing', 'Shannon Zachary': 'Librarian, Library Collection, University Library and Adjunct Lecturer in Information, School of Information', 'Fangzhou Zhang': 'PhD student', 'Xinyan Zhao': 'PhD student', 'Yixin Zou': 'PhD student'},90)
   
    total += test(num_students(data), 67, 10)

    print(total)

if __name__ == '__main__':
    main()