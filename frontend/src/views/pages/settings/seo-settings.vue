<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- /Page Header -->
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar />
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body w-100">
              <div class="content-page-header">
                <h5>SEO Settings</h5>
              </div>
              <form action="#">
                <div class="row">
                  <div class="col-lg-12 col-sm-12">
                    <div class="input-block mb-3">
                      <label>Meta Title</label>
                      <input type="text" class="form-control" placeholder="Enter Title" />
                    </div>
                  </div>
                  <div class="col-md-12 description-box">
                    <div class="input-block mb-3">
                      <label class="form-control-label">Meta Description</label>
                      <editor v-model="content" />
                    </div>
                  </div>
                  <div class="col-md-12 description-box">
                    <div class="input-block mb-3">
                      <label class="form-control-label">Meta keywords</label>
                      <editor v-model="content1" />
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="seo-setting">
                      <h6 class="mb-3">Meta Image</h6>
                      <div class="profile-picture">
                        <div class="upload-profile">
                          <div class="profile-img company-profile-img">
                            <img
                              id="company-img"
                              class="img-fluid me-0"
                              src="@/assets/img/companies/company-add-img.svg"
                              alt="profile-img"
                            />
                          </div>
                          <div class="add-profile">
                            <h5>Upload a New Photo</h5>
                            <span>Profile-pic.jpg</span>
                          </div>
                        </div>
                        <div class="img-upload">
                          <label class="btn btn-upload">
                            Upload <input type="file" />
                          </label>
                          <a class="btn btn-remove">Remove</a>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="modal-footer p-0">
                      <button
                        type="button"
                        data-bs-dismiss="modal"
                        class="btn btn-back cancel-btn me-2"
                      >
                        Cancel
                      </button>
                      <button
                        type="submit"
                        data-bs-dismiss="modal"
                        class="btn btn-primary paid-continue-btn"
                      >
                        Save Changes
                      </button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- /Page Wrapper -->
    </div>
  </div>
  <seo-settings-modal></seo-settings-modal>
</template>
<script>
import Editor from "@tinymce/tinymce-vue";
export default {
  data() {
    return {
      content: "Description",
      content1: "Description",
    };
  },
  components: {
    editor: Editor,
  },
};
</script>
