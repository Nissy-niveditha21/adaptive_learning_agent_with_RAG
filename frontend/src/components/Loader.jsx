export default function Loader({ message = 'Loading learning session...' }) {
    return (
        <div className="loader-overlay">
            <div className="loader-shell">
                <div className="spinner" />
                <p>{message}</p>
            </div>
        </div>
    );
}
