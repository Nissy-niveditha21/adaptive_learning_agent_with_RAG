import { useMemo, useState } from 'react';
import {
    startSession as fetchSession,
    evaluateAnswers
} from '../services/api';
import Hero from '../components/Hero';
import ProgressCard from '../components/ProgressCard';
import QuestionCard from '../components/QuestionCard';
import FeedbackCard from '../components/FeedbackCard';
import FeynmanCard from '../components/FeynmanCard';
import LogsCard from '../components/LogsCard';
import Loader from '../components/Loader';

const defaultSessionState = {
    topic: 'AI Learning Agent',
    current_checkpoint: {
        title: 'Initializing session…',
        completed_checkpoints: 0,
        total_checkpoints: 5,
        progress_percent: 0,
    },
    generated_questions: [],
    score: 0,
    weak_areas: [],
    feynman_explanation: '',
    messages: [],
};

export default function Dashboard() {
    const [session, setSession] = useState(null);
    const [answers, setAnswers] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [evaluation, setEvaluation] = useState(null);
    const [retryCount, setRetryCount] = useState(0);
    const [logs, setLogs] = useState([]);

    const startSession = async () => {
        setLoading(true);
        setError('');
        setEvaluation(null);

        try {
            const payload = await fetchSession();
            const normalized = {
                topic: payload.topic || 'AI Tutoring Session',
                current_checkpoint: {
                    title: payload.current_checkpoint?.title || 'Checkpoint 1: Concept Discovery',
                    completed_checkpoints: payload.current_checkpoint?.completed_checkpoints ?? payload.current_checkpoint?.completed ?? 1,
                    total_checkpoints: payload.current_checkpoint?.total_checkpoints ?? payload.current_checkpoint?.total ?? 5,
                    progress_percent: payload.current_checkpoint?.progress_percent ?? 0,
                },
                generated_questions: payload.generated_questions || [],
                score: payload.score ?? 0,
                weak_areas: payload.weak_areas || [],
                feynman_explanation: payload.feynman_explanation || '',
                messages: payload.messages || [],
            };

            setSession(normalized);
            setAnswers(new Array(normalized.generated_questions.length).fill(''));
            setLogs(['Checkpoint loaded', ...normalized.messages]);
            setRetryCount(0);
        } catch (fetchError) {
            setError('Unable to connect to the learning agent backend. Please verify the API and reload.');
            setSession(null);
            setLogs([]);
        }

        setLoading(false);
    };

    const handleAnswerChange = (index, answer) => {
        setAnswers((prev) => {
            const next = [...prev];
            next[index] = answer;
            return next;
        });
    };

    const handleEvaluateAnswers = async () => {

    if (!session) {
        setError('Please start a learning session first.');
        return;
    }

    try {

        setLoading(true);

        const result = await evaluateAnswers(answers);

        setEvaluation({
            semanticScore: Math.round(result.score * 100),
            status: result.completed ? 'Pass' : 'Retry',
            weakAreas: result.weak_areas || [],
        });

        setRetryCount(result.retry_count || 0);

        setSession((prev) => ({
            ...prev,
            score: result.score,
            weak_areas: result.weak_areas,
            feynman_explanation: result.feynman_explanation,
            messages: result.messages || [],
        }));

        setLogs((prev) => [
            ...prev,
            ...(result.messages || []),
        ]);

    } catch (err) {

        setError("Evaluation failed.");

    } finally {

        setLoading(false);
    }
};

    const progress = useMemo(() => {
        const checkpoint = session?.current_checkpoint;
        if (!checkpoint) return 0;
        const total = checkpoint.total_checkpoints || 5;
        const completed = checkpoint.completed_checkpoints || 0;
        return checkpoint.progress_percent ?? Math.round((completed / total) * 100);
    }, [session]);

    return (
        <div className="dashboard-shell">
            <Hero onStartSession={startSession} loading={loading} />

            {loading && <Loader />}

            {error && (
                <div className="alert-card glass-card">
                    <strong>Connection issue</strong>
                    <p>{error}</p>
                </div>
            )}

            <div className="dashboard-grid">
                <div className="dashboard-left">
                    <ProgressCard
                        topic={session?.topic}
                        checkpoint={session?.current_checkpoint?.title}
                        completed={session?.current_checkpoint?.completed_checkpoints}
                        total={session?.current_checkpoint?.total_checkpoints}
                        score={session?.score}
                        progress={progress}
                    />

                    <section className="panel-card question-panel glass-card">
                        <div className="panel-heading">
                            <div>
                                <span className="eyebrow">Question Panel</span>
                                <h2>Generated study prompts</h2>
                            </div>
                            <button className="button button-secondary" onClick={handleEvaluateAnswers}>
                                Evaluate Answers
                            </button>
                        </div>

                        <div className="questions-list">
                            {session?.generated_questions?.length ? (
                                session.generated_questions.map((question, index) => (
                                    <QuestionCard
                                        key={index}
                                        index={index}
                                        question={question}
                                        answer={answers[index] || ''}
                                        onChange={(value) => handleAnswerChange(index, value)}
                                    />
                                ))
                            ) : (
                                <p className="hint-text">Start a session to generate checkpoint questions.</p>
                            )}
                        </div>
                    </section>
                </div>

                <div className="dashboard-right">
                    <FeedbackCard
                        semanticScore={evaluation?.semanticScore ?? session?.score}
                        status={evaluation?.status || 'Awaiting answers'}
                        weakAreas={evaluation?.weakAreas || session?.weak_areas}
                        retryCount={retryCount}
                    />

                    <FeynmanCard explanation={session?.feynman_explanation} />

                    <LogsCard messages={logs} />
                </div>
            </div>
        </div>
    );
}
