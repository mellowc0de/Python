class Datacenter:    
    def __init__(self):
        """Initialize the Datacenter class. Input data for DC name, state, 
        city, manager, and pod count.
        """
        self.name=input("Add DC name:  ").upper();
        self.state=input("Add DC state:  ").upper();
        self.city=input("Add DC city:  ").upper();
        self.manager=input("Add DC manager: ").upper();
        self.pods=int(input("How many PODs?  "));  # type: ignore
        self.rows=int(input("How many ROWs in the DC?  "));  # type: ignore
        
    def dc_pods(self):
        """Uses self.pods integer as the dc pod count as well as to form 
        the names that are appended to dc_pod_list
        """
        dc_pod_count = self.pods

        try:
            if type(dc_pod_count) is int:
                # DC POD List collects pod names from data input of self.pods
                dc_pod_list = []
                
                for pod_int in (n+1 for n in range(dc_pod_count)):
                    pod_int = "POD" + str(pod_int)
                    dc_pod_list.append(pod_int)
                    
                    print(dc_pod_list) # print statement for testing purposes
            else:
                print("not a valid number")

        except TypeError:
            print("Input must be an integer")
    
    def dc_rows(self):
        """Uses self.rows to determine the total number of rows in the Datacenter.
        """
        dc_rows_count = self.rows

        try:
            if type(dc_rows_count) is int:
                # DC POD List collects pod names from data input of self.pods
                dc_rows_list = []
                
                for row_int in (n+1 for n in range(dc_rows_count)):
                    row_int = "ROW" + str(row_int)
                    dc_rows_list.append(row_int)
                    
                    print(dc_rows_list) # print statement for testing purposes
            else:
                print("not a valid number")

        except TypeError:
            print("Input must be an integer")
    
    def pod(self):
        """Defines the PODs and their respective rows in the Datacenter
        """
        
      
dc = Datacenter()

print(dc)
print(dc.dc_pods())
print(dc.dc_rows())