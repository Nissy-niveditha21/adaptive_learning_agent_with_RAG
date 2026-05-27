import Navbar from './Navbar';

export default function Layout({ children }) {
    return (
        <div className="app-shell">
            <Navbar />
            <div className="page-wrapper">{children}</div>
        </div>
    );
}
