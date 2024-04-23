import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

interface FeatureItem {
    title: string;
    subtitle: string;
    Gif: string;
    description: JSX.Element;
  };


const FeatureList: FeatureItem[] = [
  {
    title: 'Introducing Sparky',
    subtitle: 'A high-dynamic robotic dog with a combination of interactivity and extensibility',
    description: (
      <>SPARKY is a nimble and agile robotic companion equipped with a Cortex-A7 1GHz processor. By prioritizing aesthetics and user experience,<br/>we have refined SPARKY's design and structure over the years. Its legs feature modular linkages and integrate an AIA actuator unit, allowing you to upgrade SPARKY's power system as easily as changing a four-wheel drive car motor and customize a one-of-a-kind SPARKY just like swapping phone cases.</>
    ),
    Gif: 'img/sparky.gif',
  },
];

function Feature({title, subtitle, description, Gif}: FeatureItem) {
  return (
    <div className={clsx('col col--12')}>
    <div className="text--center">
      <Heading as="h1" style={{ color: 'white',marginBottom: '20px' }}>{title}</Heading>
      <Heading as="h2" style={{ color: 'white',marginBottom: '30px' }}>{subtitle}</Heading>
      <div className="text--center padding-horiz--md" style={{ color: 'white' }}>
    </div>
      <img src={Gif} alt={title} className={styles.featureGif} role="img" style={{ borderRadius: '10px', marginBottom: '20px'}}/>
    </div>
    <Heading as="p" style={{color: 'white', marginTOP: '30px'}}>
        {description}</Heading>
  </div>
);
}

export default function HomepageFeatures(): JSX.Element {
  return (
     <section className={styles.features}>
      <div className={clsx('hero hero')} style={{ backgroundColor: 'rgb(28 28 28)' }}>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
