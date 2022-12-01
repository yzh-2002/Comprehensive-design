import React,{ useState } from "react"
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  UploadOutlined,
  UserOutlined,
  VideoCameraOutlined,
} from '@ant-design/icons';
import { Layout, Menu, Image } from 'antd';
const { Header, Sider, Content } = Layout;

import "@/style/layout.css"

import HeaderImage from "@/assets/header.png"
import LogoImage from "@/assets/logo.png"

function App() {
  const [collapsed,setCollapsed] =useState(false);

  return (
    <Layout style={{height:"100%"}}>
      <Sider trigger={null} collapsible collapsed={collapsed}
        breakpoint="md"
        onBreakpoint ={(broken)=>{
          setCollapsed(broken)
        }}
      >
        <div className="logo">
          <Image
            preview={false}
            src={!collapsed ? HeaderImage : LogoImage}
          ></Image>
        </div>
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={['1']}
          items={[
            {
              key: '1',
              icon: <UserOutlined />,
              label: 'nav 1',
            },
            {
              key: '2',
              icon: <VideoCameraOutlined />,
              label: 'nav 2',
            },
            {
              key: '3',
              icon: <UploadOutlined />,
              label: 'nav 3',
            },
          ]}
        >
        </Menu>
      </Sider>
      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 0 }}>
          {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
            className: 'trigger',
            onClick: () => setCollapsed(!collapsed),
          })}
        </Header>
        <Content
          className="site-layout-background" 
          style={{
            margin: '24px 16px',
            padding: 24,
            minHeight: 280,
          }}
        >
          Content
        </Content>
      </Layout>
    </Layout>
  )
}

export default App
