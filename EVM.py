#====================== Data Voter===================== 
voter = [
    {
        'voter_id': 1001,
        'name': 'shivam',
        'vote_status': False
    },
    {
        'voter_id': 1002,
        'name': 'sachin',
        'vote_status': False   
    },
    {    'voter_id': 1003,
        'name': 'deepak',
        'vote_status': False
    },
    {    'voter_id': 1004,
        'name': 'akansha',
        'vote_status': False
    },
    {    'voter_id': 1005,
        'name': 'karan',
        'vote_status': False
    },
    {    'voter_id': 1006,
        'name': 'ravi',
        'vote_status': False
    },
    {    'voter_id': 1007,
        'name': 'sanjay',
        'vote_status': False
    },
    {    'voter_id': 1008,
        'name': 'rohan',
        'vote_status': False
    },
    {    'voter_id': 1009,
        'name': 'shyam',
        'vote_status': False
    },
    {    'voter_id': 10010,
        'name': 'seema',
        'vote_status': False
    }
]
# ==================== Vote Stores in variable of every Parties====================================

vote_bjp = 0
vote_cog = 0
vote_aap = 0
vote_bsp = 0
vote_cpim = 0
vote_npp= 0
vote_nota = 0

# ===================== This Result() function is Print Election Result=================================

def result():
    print('\n\n\n\n\t\t\t\t\t\t\t\t<--------------Result 2024 Election----------->')
    print(f"\n\n\n\t\t\t\t\tBharti Janta Party votes:{vote_bjp}\n\t\t\t\t\tIndian National Congrees Votes:{vote_cog}\n\t\t\t\t\tAam Aadmi Party votes:{vote_aap}\n\t\t\t\t\tBahujan Samaj Party votes:{vote_bsp}\n\t\t\t\t\tCPI(M) Communist Party of India(Maxist) votes:{vote_cpim}\n\t\t\t\t\tNational  People's Party votes:{vote_npp}\n\t\t\t\t\tNOTA votes:{vote_nota}")


#  ======================== This function is body EVM Program =======================

def vote():
    
    for i in range(len(voter)+1):
        if voter_id == voter[i]['voter_id']:
            find = i
            break
            


    if voter[find]['vote_status'] == False:
            print("\n\n\n\t\t\t\t\t\t\t\t Prees 1 for Bharti Janta Party\n\t\t\t\t\t\t\t\t",
            "Prees 2 for Indian National Congress\n\t\t\t\t\t\t\t\t",
            "Prees 3 for Aam Aadmi Party\n\t\t\t\t\t\t\t\t",
            "Prees 4 for Bahujan samaj party\n\t\t\t\t\t\t\t\t",
            "Prees 5 for CPI(M) Communist Party of India(Maxist)\n\t\t\t\t\t\t\t\t",
            "Prees 6 for National People's Party\n\t\t\t\t\t\t\t\t",
            "Press 7 for Nota ") 
            choice = int(input(f"\n\n\n\t\t\t\t\t\t\t\t{voter[find]['name']} Give your Vote:"))
            global vote_bjp
            global vote_cog
            global vote_aap
            global vote_bsp
            global vote_cpim
            global vote_nota
            global vote_npp

            match choice:
                case 1:  
                    vote_bjp +=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")
                case 2:
                    
                    vote_cog+=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")    
                case 3:
                    
                    vote_aap+=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")
                case 4:
                    
                    vote_bsp+=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")
                case 5:
                    
                    vote_cpim+=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")
                case 6:
                    
                    vote_npp+=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")                
                case 7:
                   
                    vote_nota+=1
                    print("\n\n\n\n\t\t\t\t\t\t\t\tYour Vote has been Successful cast")    
                case _:
                    print('\n\n\n\n\t\t\t\t\t\t\t\tinvalid choice')
    
            if choice<8:    
                voter[find]['vote_status'] = True
                
    else:
        print('\n\n\t\t\t\t\t\t\t\tVote Two Times is Punishable offence\n\t\t\t\t\t\t\t\tPunishment are 1 year of Imprisonment or 1 lakh Rupee Fine.\n')
    print('\n\n\n\t\t\t\t\t\t\t\t\t<-----------Next voter Turn------------>')     
    menu()       

# ========================== This function is head EVM Program ===================

# ====================This function is check voter id .Given by user


def menu():
    try:
        print(f'\n\t\t\t\t\t\t\t\t\t<---------For Result Type 2024--------->')
        print(f'\n\t\t\t\t\t\t\t\t\t<---------For Exit Type 2000--------->')
        
        global voter_id
        voter_id = int(input('\n\n\n\n\n\t\t\t\t\t\t\t\tplease enter your voter id here:'))
        if voter_id == 2000:
            exit()     

        if voter_id == 2024:
             result()
        else: 
            for i in range(len(voter)+1):
                    if voter_id == voter[i]['voter_id']:
                        vote()
                        break
            
    except:
        print('\n\n\n\t\t\t\t\t\t\t\tYou are name is not Add in voter list!') 
        menu()

print(f'\n\n\n\t\t\t\t\t\t\t\t<--------------Welcome To 2024 Election--------------->')
menu()
