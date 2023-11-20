import swal from 'sweetalert';

export const useMessage = (error) =>{

    const errorMessage = () =>{
        if (error != null) {
            swal({
                title: "Error",
                text: error,
                icon: "error",
                button: "Ok!",
              });
        }
    }

    return {
        errorMessage
    }
}

