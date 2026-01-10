import React from 'react';
import { Package, Database, Server, Globe } from 'lucide-react';

const Header = () => {
  return (
    <div className="header-container">
      <div className="header-title">
        <Package className="header-icon" size={36} />
        <h1>3-Tier Product Management System</h1>
      </div>
      
      <div className="architecture-info">
        <div className="tier-card tier-presentation">
          <Globe size={20} />
          <div>
            <h3>Tier 1: Presentation</h3>
            <p>React UI Layer</p>
          </div>
        </div>
        
        <div className="tier-card tier-application">
          <Server size={20} />
          <div>
            <h3>Tier 2: Application</h3>
            <p>Flask API Layer</p>
          </div>
        </div>
        
        <div className="tier-card tier-data">
          <Database size={20} />
          <div>
            <h3>Tier 3: Data</h3>
            <p>SQLite Database</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;
