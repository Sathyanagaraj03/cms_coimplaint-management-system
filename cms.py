# Complaint class to store complaint details
class Complaint:
  def store(self, complaint_id, title, description, status):
     self.complaint_id = complaint_id
     self.title = title
     self.description = description
     self.status = status
#**************************************** class cms declaration************************************************

class CMS:
   complaints = []
#**************************************** register coimplaint function************************************************

   def register_complaint(self, title, description):
    complaint_id = len(self.complaints) + 1
    status = "Registered"
    complaint = Complaint()
    c=complaint.store(complaint_id, title, description, status)
    self.complaints.append(complaint)
    print("**********************************")
    print("Complaint registered successfully!")
    print("**********************************")
#**************************************** view the complaints************************************************

   def view_complaints(self):
     if not self.complaints:
       print("**********************************")
       print("No complaints registered.")
       print("**********************************")
     else: 
        for complaint in self.complaints:
           print("**********************************")
           print(f"Complaint ID: {complaint.complaint_id}")
           print(f"Title: {complaint.title}")
           print(f"Description: {complaint.description}")
           print(f"Status: {complaint.status}")
           print("**********************************")
#**************************************** update the complaints************************************************

   def update_complaint_status(self, complaint_id, new_status):
     for complaint in self.complaints:
         if complaint.complaint_id == complaint_id:
             complaint.status = new_status
             print("**********************************")
             print("Complaint status updated successfully!")
             print("**********************************")
     return
#**************************************** main function************************************************
def main():
  cms = CMS()
  while True:
   print("\nComplaint Management System")
   print("1. Register Complaint")
   print("2. View Complaints")
   print("3. Update Complaint Status")
   print("4. Exit")
   choice = input("Enter your choice: ")
   if choice == "1":
      title = input("Enter complaint title: ")
      description = input("Enter complaint description: ")
      cms.register_complaint(title, description)
   elif choice == "2":
         cms.view_complaints()
   elif choice == "3":
       complaint_id = int(input("Enter complaint ID: "))
       new_status = input("Enter new status: ")
       cms.update_complaint_status(complaint_id, new_status)
   elif choice == "4":
      print("Exiting the Complaint Management System...")
      break
   else:
       print("Invalid choice. Please try again.")


if __name__ == '__main__':

   main()