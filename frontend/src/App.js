import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentTable = () => {
  const [students, setStudents] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [workers, setWorkers] = useState([]);
  const [salaries, setSalaries] = useState([]);

  useEffect(() => {
    axios.get("backend url")
      .then(response => {
        setStudents(response.data.studentlist);
      })
      .catch(error => {
        console.error('Error fetching student data:', error);
      });

    axios.get("backend url/employeelist")
      .then(response => {
        setEmployees(response.data.employeelist);
      })
      .catch(error => {
        console.error('Error fetching employee data:', error);
      });

    axios.get("backend url/workerlist")
      .then(response => {
        setWorkers(response.data.workerlist);
      })
      .catch(error => {
        console.error('Error fetching workers data:', error);
      });

    axios.get("backend url/salarylist")
      .then(response => {
        setSalaries(response.data.salarylist);
      })
      .catch(error => {
        console.error('Error fetching salaries data:', error);
      });
  }, []);

  const tableHeaderStyle = {
    backgroundColor: '#333',
    color: '#fff',
    padding: '10px',
    textAlign: 'left',
  };

  const tableCellStyle = {
    padding: '10px',
    borderBottom: '1px solid #ccc',
  };

  return (
    <div style={{ backgroundColor: '#f2f2f2', padding: '20px' }}>
      <h1 style={{ color: '#333', marginBottom: '20px' }}>Student List</h1>
      {/* Student list table */}
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Roll</th>
            <th style={tableHeaderStyle}>Grade</th>
          </tr>
        </thead>
        <tbody>
          {students.map(student => (
            <tr key={student.id}>
              <td style={tableCellStyle}>{student.name}</td>
              <td style={tableCellStyle}>{student.roll}</td>
              <td style={tableCellStyle}>{student.grade}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h1 style={{ color: '#333', marginTop: '40px', marginBottom: '20px' }}>Employee List</h1>
      {/* Employee list table */}
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Employee_id</th>
            <th style={tableHeaderStyle}>Department</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(employee => (
            <tr key={employee.id}>
              <td style={tableCellStyle}>{employee.name}</td>
              <td style={tableCellStyle}>{employee.employee_id}</td>
              <td style={tableCellStyle}>{employee.department}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h1 style={{ color: '#333', marginBottom: '20px' }}>Worker List</h1>
      {/* Worker list table */}
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Worker_id</th>
            <th style={tableHeaderStyle}>Job_title</th>
          </tr>
        </thead>
        <tbody>
          {workers.map(worker => (
            <tr key={worker.id}>
              <td style={tableCellStyle}>{worker.name}</td>
              <td style={tableCellStyle}>{worker.worker_id}</td>
              <td style={tableCellStyle}>{worker.job_title}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h1 style={{ color: '#333', marginTop: '40px', marginBottom: '20px' }}>Salary List</h1>
      {/* Salary list table */}
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Roll_id</th>
            <th style={tableHeaderStyle}>Salary</th>
          </tr>
        </thead>
        <tbody>
          {salaries.map(salary => (
            <tr key={salary.id}>
              <td style={tableCellStyle}>{salary.name}</td>
              <td style={tableCellStyle}>{salary.roll_id}</td>
              <td style={tableCellStyle}>{salary.salary}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StudentTable;
