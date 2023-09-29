import { Modal, Tabs } from 'antd';
import PropTypes from 'prop-types';

const Edit = ({ activeTab, isModalOpen, setActiveTab, setIsModalOpen }) => {
  const handleModal = () => {
    setIsModalOpen((prev) => !prev);
  };
  return (
    <Modal open={isModalOpen} onCancel={handleModal}>
      <h2></h2>
      <Tabs
        activeKey={activeTab}
        onChange={(activeKey) => setActiveTab(activeKey)}
        items={[
          {
            label: 'students',
            key: 'students',
          },
          {
            label: 'teachers',
            key: 'teachers',
          },
          { label: 'departments', key: 'departments' },
        ]}
      />
    </Modal>
  );
};

Edit.propTypes = {
  activeTab: PropTypes.string,
  setActiveTab: PropTypes.func,
  isModalOpen: PropTypes.bool,
  setIsModalOpen: PropTypes.fumc,
};

export default Edit;
