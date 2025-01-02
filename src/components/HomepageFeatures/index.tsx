import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Translate from '@docusaurus/Translate';

interface FeatureItem {
    title: string;
    subtitle: string;
    Gif: string;
    description: JSX.Element;
  };


const FeatureList: FeatureItem[] = [
  {
    title: '',
    subtitle: (<Translate>消费级高动态AI仿生机器人平台</Translate>),
    description: (
    <Translate>哮天是 Hengbot 推出的首款消费级高动态AI智能仿生陪伴机器狗，它结合了高级外观设计、灵巧高速运动能力和便捷二次开发功能，使用户能够轻松体验AI+机器人技术的魅力。</Translate>
    ),
    Gif: 'img/Sirius.gif',
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
