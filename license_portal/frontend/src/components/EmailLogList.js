import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EmailLogList = () => {
  const [emailLogs, setEmailLogs] = useState([]);

  useEffect(() => {
    axios.get('/api/licenses/lista_correos_enviados/5/') // Endpoint de Django
      .then(response => {
        setEmailLogs(response.data);
      })
      .catch(error => {
        console.error('Error al obtener los registros de correos:', error);
      });
  }, []);

  return (
    <div>
      <h2>Registros de Correos</h2>
      <ul>
        {emailLogs.map(log => (
          <li key={log.id}>
            Enviado en: {log.sent_at} - Licencia ID: {log.license_id}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmailLogList;
