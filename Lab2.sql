/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/5/6 22:35:22                            */
/*==============================================================*/
drop database if exists Bank;
create database Bank;
use Bank;

drop table if exists Account;

drop table if exists CheckAccount;

drop table if exists Customer;

drop table if exists Customer_CheckAccount;

drop table if exists Customer_DepositAccount;

drop table if exists Department;

drop table if exists DepositAccount;

drop table if exists Employee;

drop table if exists Employee_Customer;

drop table if exists Loan;

drop table if exists Loan_Customer;

drop table if exists Pay;

drop table if exists SubBank;

/*==============================================================*/
/* Table: Account                                               */
/*==============================================================*/
create table Account
(
   Account_ID           decimal(16) not null,
   Account_Money        float,
   Account_RegDate      date,
   Account_RegBank      char(50),
   primary key (Account_ID)
);

/*==============================================================*/
/* Table: CheckAccount                                          */
/*==============================================================*/
create table CheckAccount
(
   Account_ID           decimal(16) not null,
   Account_Money        float,
   Account_RegDate      date,
   Account_RegBank      char(50),
   Overdraft            float,
   primary key (Account_ID)
);

/*==============================================================*/
/* Table: Customer                                              */
/*==============================================================*/
create table Customer
(
   User_ID              decimal(50) not null,
   User_Name            char(32),
   User_Phone           decimal(20),
   User_Address         char(128)DEFAULT NULL,
   User_Contact_Name    char(32)DEFAULT NULL,
   User_Contact_Phone   decimal(20)DEFAULT NULL,
   User_Contact_Email   char(64)DEFAULT NULL,
   User_Contact_Relation char(32)DEFAULT NULL,
   primary key (User_ID)
);

/*==============================================================*/
/* Table: Customer_CheckAccount                                 */
/*==============================================================*/
create table Customer_CheckAccount
(
   User_ID              decimal(50) not null,
   Bank_Name            char(50) not null,
   Account_ID           decimal(16) not null,
   LastView_C           date,
   primary key (User_ID, Bank_Name)
);

/*==============================================================*/
/* Table: Customer_DepositAccount                               */
/*==============================================================*/
create table Customer_DepositAccount
(
   User_ID              decimal(50) not null,
   Bank_Name            char(50) not null,
   Account_ID           decimal(16) not null,
   LastView_D           date,
   primary key (User_ID, Bank_Name)
);

/*==============================================================*/
/* Table: Department                                            */
/*==============================================================*/
create table Department
(
   Department_ID        decimal(6) not null,
   Bank_Name            char(50) not null,
   Department_Name      char(50),
   Department_Type      char(16),
   Department_Leader    decimal(16) not null,
   primary key (Department_ID),
   UNIQUE KEY (Department_Leader)
);

/*==============================================================*/
/* Table: DepositAccount                                        */
/*==============================================================*/
create table DepositAccount
(
   Account_ID           decimal(16) not null,
   Account_Money        float,
   Account_RegDate      date,
   Account_RegBank      char(50),
   InterestRate         float,
   Currencytype         char(16),
   primary key (Account_ID)
);

/*==============================================================*/
/* Table: Employee                                              */
/*==============================================================*/
create table Employee
(
   Employee_ID          decimal(16) not null,
   Department_ID        decimal(6) not null,
   Employee_Name        char(32),
   Employee_Phone       decimal(12),
   Employee_Address     char(128),
   Employee_EnterDate   date,
   primary key (Employee_ID)
);

/*==============================================================*/
/* Table: Employee_Customer                                     */
/*==============================================================*/
create table Employee_Customer
(
   Employee_ID          decimal(16) not null,
   User_ID              decimal(16) not null,
   ServiceType          char(16),
   primary key (Employee_ID, User_ID)
);

/*==============================================================*/
/* Table: Loan                                                  */
/*==============================================================*/
create table Loan
(
   Loan_ID              decimal(16) not null,
   Bank_Name            char(50) not null,
   Loan_Money           float,
   primary key (Loan_ID)
);

/*==============================================================*/
/* Table: Loan_Customer                                         */
/*==============================================================*/
create table Loan_Customer
(
   Loan_ID              decimal(16) not null,
   User_ID              decimal(50) not null,
   primary key (Loan_ID, User_ID)
);

/*==============================================================*/
/* Table: Pay                                                   */
/*==============================================================*/
create table Pay
(
   Loan_ID              decimal(16) not null,
   Pay_Date             date,
   Pay_Money            float
);

/*==============================================================*/
/* Table: SubBank                                               */
/*==============================================================*/
create table SubBank
(
   Bank_Name            char(50) not null,
   City                 char(50),
   Possession           float,
   primary key (Bank_Name)
);

alter table CheckAccount add constraint FK_Account_CheckAccount foreign key (Account_ID)
      references Account (Account_ID) on delete restrict on update restrict;

alter table Customer_CheckAccount add constraint FK_CheckAccount_UPONE foreign key (Account_ID)
      references CheckAccount (Account_ID) on delete restrict on update restrict;

alter table Customer_CheckAccount add constraint FK_Customer_Check foreign key (User_ID)
      references Customer (User_ID) on delete restrict on update restrict;

alter table Customer_CheckAccount add constraint FK_SubBank_Check foreign key (Bank_Name)
      references SubBank (Bank_Name) on delete restrict on update restrict;

alter table Customer_DepositAccount add constraint FK_Customer_Deposit foreign key (User_ID)
      references Customer (User_ID) on delete restrict on update restrict;

alter table Customer_DepositAccount add constraint FK_DepositAccount_UPONE foreign key (Account_ID)
      references DepositAccount (Account_ID) on delete restrict on update restrict;

alter table Customer_DepositAccount add constraint FK_SubBank_Deposit foreign key (Bank_Name)
      references SubBank (Bank_Name) on delete restrict on update restrict;

alter table Department add constraint FK_SubBank_Department foreign key (Bank_Name)
      references SubBank (Bank_Name) on delete restrict on update restrict;

alter table DepositAccount add constraint FK_Account_DepositAccount foreign key (Account_ID)
      references Account (Account_ID) on delete restrict on update restrict;

alter table Employee add constraint FK_Employee_Department foreign key (Department_ID)
      references Department (Department_ID) on delete restrict on update restrict;

alter table Employee_Customer add constraint FK_Employee_Customer foreign key (Employee_ID)
      references Employee (Employee_ID) on delete restrict on update restrict;

alter table Employee_Customer add constraint FK_Employee_Customer2 foreign key (User_ID)
      references Customer (User_ID) on delete restrict on update restrict;

alter table Loan add constraint FK_Loan_SubBank foreign key (Bank_Name)
      references SubBank (Bank_Name) on delete restrict on update restrict;

alter table Loan_Customer add constraint FK_Loan_Customer foreign key (Loan_ID)
      references Loan (Loan_ID) on delete restrict on update restrict;

alter table Loan_Customer add constraint FK_Loan_Customer2 foreign key (User_ID)
      references Customer (User_ID) on delete restrict on update restrict;

alter table Pay add constraint FK_Loan_Pay foreign key (Loan_ID)
      references Loan (Loan_ID) on delete restrict on update restrict;



insert into subbank value("合肥支行","合肥",10000000000);
insert into subbank value("上海支行","上海",10000000000);

