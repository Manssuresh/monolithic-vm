import React, { useState } from 'react';

function App() {
  const [studentTable, setStudentTable] = useState('');

  const handleClick = async () => {
    const response = await fetch(process.env.REACT_APP_BACKEND_URL);
    const result = await response.text();
    setStudentTable(result);
  };

  return (
    <>
      <h1>Welcome to the Student List</h1>
      <button onClick={handleClick}>Get Student List</button>
      <div dangerouslySetInnerHTML={{ __html: studentTable }} />
    </>
  );
}

export default App;
