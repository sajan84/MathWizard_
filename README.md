# MathWizard_

drop table Customer;
drop table AccountType;
drop table Account;
drop table TransactionInfo;


Create Table Customer(
customerId INT identity primary key,
customerFirstName VARCHAR(30) not null,
customerLastName VARCHAR(30) not null,
customerAddress VArchar(200),
customerMobile varchar(15) unique,
customerAdharCard  varchar(12) unique
);

Insert Into Customer(customerFirstName,customerLastName,customerAddress,customerMobile,customerAdharCard) values
('Sajan','Pande','XYZ','6354177152','380427137078'),
('Harsh','Dhorajiya','Epz','6352182943','380452139876')

Create Table AccountType(
accountTypeId INT identity Primary key,
typeName Varchar(50) not null,
interestRate Decimal(5,2) not null
);

Insert Into AccountType(typeName,interestRate) values
('Saving',4.2),
('Current',0.4)

Create Table Account(
accountId INT Primary key identity,
accountNumber varchar(12) unique not null,
customerId INT,
accountTypeId INT,
balance Decimal(10,2) not null,
foreign key(customerId) References Customer(customerId),
foreign key(accountTypeId) References AccountType(accountTypeId)
);

Insert Into Account (accountNumber,customerId,accountTypeId,balance)Values
('524168004563',1,1,6000),
('524168004564',2,2,8000),
('524168004565',1,2,9000)

Create Table TransactionInfo(
transactionID INT Primary key identity,
accountId INT,
transactionType varchar(50),
amount Decimal(10,2),
transactionDate TimeStamp,
foreign key (accountId) References Account(accountId)
);


 public async Task<ResponseDto> GetCustomer(int id)
 {
     var customer = await _context.Customers.FindAsync(id);
     if (customer == null)
     {
         return null;
     }

     try
     {
         

         var res = await _context.Customers
             .Where(customer => customer.CustomerId == id) // Filter by specific customer ID
             .GroupJoin(
                 _context.Accounts,
                 customer => customer.CustomerId,
                 account => account.CustomerId,
                 (customer, accounts) => new { Customer = customer, Accounts = accounts }
             )
             .SelectMany(
                 group => group.Accounts.DefaultIfEmpty(),
                 (group, account) => new GetcustomerDto()
                 {
                     CustomerId = group.Customer.CustomerId,
                     CustomerFirstName = group.Customer.CustomerFirstName,
                     CustomerLastName = group.Customer.CustomerLastName,
                     CustomerMobile = group.Customer.CustomerMobile,
                     CustomerAddress = group.Customer.CustomerAddress,
                     CustomerAdharCard = group.Customer.CustomerAdharCard,
                     Balance = account != null ? account.Balance : 0, // Default to 0 if account is null
                     AccountNumber = account != null ? account.AccountNumber : null, // Default to null if account is null
                     AccountType = account != null ? account.AccountType.TypeName : null // Default to null if account is null
                 }
             )
             .ToListAsync();

         responseDto.result = res;
         return responseDto;


         // responseDto.result = customer;
       
     }
     catch (Exception ex)
     {
         responseDto.isResult = "false";
         responseDto.Message = ex.Message;
         return responseDto;

     }

















































































































































