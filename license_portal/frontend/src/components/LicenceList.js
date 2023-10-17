import React, { useState, useEffect } from 'react';
import axios from 'axios';

const LicenseList = () => {
  const [licenses, setLicenses] = useState([]);

  useEffect(() => {
    axios.get('/api/licenses/') // Endpoint de Django
      .then(response => {
        setLicenses(response.data);
      })
      .catch(error => {
        console.error('Error al obtener las licencias:', error);
      });
  }, []);

  return (
    <div>
      <h2>Licencias</h2>
      <ul>
        {licenses.map(license => (
          <li key={license.id}>
            ID: {license.id} - Tipo: {license.license_type}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LicenseList;
