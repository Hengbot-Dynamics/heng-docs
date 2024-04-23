import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import HomepageFeatures1 from '@site/src/components/HomepageFeatures1';
import HomepageFeatures2 from '@site/src/components/HomepageFeatures2';
import HomepageFeatures3 from '@site/src/components/HomepageFeatures3';
import HomepageFeatures4 from '@site/src/components/HomepageFeatures4';
import HomepageFeatures5 from '@site/src/components/HomepageFeatures5';
import HomepageFeatures6 from '@site/src/components/HomepageFeatures6';
import Heading from '@theme/Heading';
import Translate from '@docusaurus/Translate';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--dark', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className={clsx("button button--secondary button--lg button")}
            to="https://sparky.hengbot.com/pages/sparky">
            Buy Now⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}



export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <div style={{ backgroundColor: 'rgb(28 28 28)' }} >
        <HomepageHeader />
        <main>
          <HomepageFeatures />
        </main>
        <main>
          <HomepageFeatures1 />
        </main>
        <main>
          <HomepageFeatures2 />
        </main>
        <main>
          <HomepageFeatures3 />
        </main>
        <main>
          <HomepageFeatures4 />
        </main>
        <main>
          <HomepageFeatures5 />
        </main>
        <section>
        <h2>Software Capability</h2>
</section>
        <main>
          <HomepageFeatures6 />
        </main>
      </div>
    </Layout>
  );
}
