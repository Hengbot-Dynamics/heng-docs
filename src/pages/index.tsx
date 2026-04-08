import React, { useEffect } from 'react';
import Head from '@docusaurus/Head';

export default function Home(): JSX.Element {
  useEffect(() => {
    // 确保在客户端执行跳转（兜底方案）
    window.location.replace("https://user.hengbot.com/zh/heng-docs/intro");
  }, []);

  return (
    <>
      <Head>
        {/* 利用静态生成的 meta 标签实现瞬间重定向，对 SEO 更友好且跳转速度极快 */}
        <meta http-equiv="refresh" content="0; url=https://user.hengbot.com/zh/heng-docs/intro" />
        <title>Redirecting to new documentation...</title>
      </Head>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#1c1c1c', color: '#fff', fontFamily: 'system-ui, sans-serif' }}>
        <p>正在跳转至全新文档中心，请稍候...</p>
        <p>Redirecting to the new documentation center, please wait...</p>
      </div>
    </>
  );
}
