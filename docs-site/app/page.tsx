import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">Anvesh Documentation</h1>
      <p className="mb-8 text-xl">
        Automated Intelligence Engine that hunts for high-value businesses.
      </p>
      <Link
        href="/docs"
        className="px-6 py-3 bg-foreground text-background rounded-lg font-semibold hover:opacity-90"
      >
        Open Documentation
      </Link>
    </main>
  );
}
