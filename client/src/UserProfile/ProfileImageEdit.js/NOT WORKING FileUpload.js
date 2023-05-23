import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Center, useColorModeValue, Icon } from '@chakra-ui/react';
import { AiFillFileAdd } from 'react-icons/ai';

export const  FileUpload=({ onFileAccepted })=> {
  const onDrop = useCallback((acceptedFiles) => {
    onFileAccepted(acceptedFiles[0]);
  }, [onFileAccepted]);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop, accept: '.torrent', maxFiles: 1, multiple: false,
  });

  const dropText = isDragActive ?  'Drop the files here ...' : 'Drag your selected image into here, or click to select files';

  const activeBg = useColorModeValue('gray.100', 'gray.600');
  const borderColor = useColorModeValue(
    isDragActive ? 'teal.900' : 'gray.400',
    isDragActive ? 'Black.500' : 'Black.500',
  );

  return (
    <Center
      p={10}
      width='50%'
      cursor="pointer"
      
      bg={isDragActive ? activeBg : 'transparent'}
      _hover={{ bg: '#2A2A2A' }}
      transition="background-color 0.3s ease"
      borderRadius={4} 
      border="3px dashed"
      borderColor={borderColor}
      {...getRootProps()}
    >
      <input {...getInputProps()} />
      <Icon as={AiFillFileAdd}  />
      <p >{dropText} </p>
    </Center>
  );
}