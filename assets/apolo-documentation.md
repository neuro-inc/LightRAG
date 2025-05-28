Directory Structure:

└── ./
    ├── apolo-actions
    │   ├── reference
    │   │   ├── checkout.md
    │   │   ├── filebrowser.md
    │   │   ├── jupyter.md
    │   │   ├── remote-debug.md
    │   │   ├── tensorboard.md
    │   │   ├── vs-code.md
    │   │   └── webdav-server.md
    │   ├── README.md
    │   └── SUMMARY.md
    ├── apolo-python-sdk
    │   ├── README.md
    │   └── SUMMARY.md
    ├── docs
    │   ├── administration
    │   │   ├── cluster-management
    │   │   │   ├── creating-a-cluster.md
    │   │   │   ├── creating-node-pools.md
    │   │   │   ├── managing-organizations.md
    │   │   │   ├── managing-presets.md
    │   │   │   ├── managing-users-and-quotas.md
    │   │   │   ├── README.md
    │   │   │   └── reports.md
    │   │   └── overview-and-installation
    │   │       ├── architecture-overview.md
    │   │       ├── on-premise-installation-guide.md
    │   │       └── README.md
    │   ├── apolo-concepts-cli
    │   │   ├── apps
    │   │   │   ├── files.md
    │   │   │   ├── images.md
    │   │   │   ├── jobs.md
    │   │   │   └── README.md
    │   │   └── installing.md
    │   ├── apolo-console
    │   │   ├── apps
    │   │   │   ├── available-apps
    │   │   │   │   ├── llm-inference
    │   │   │   │   │   ├── multi-gpu-benchmarks-report.md
    │   │   │   │   │   ├── README.md
    │   │   │   │   │   └── vllm-inference-details.md
    │   │   │   │   ├── apolo-deploy.md
    │   │   │   │   ├── dify.md
    │   │   │   │   ├── fooocus.md
    │   │   │   │   ├── jupyter-lab.md
    │   │   │   │   ├── jupyter-notebook.md
    │   │   │   │   ├── ml-flow.md
    │   │   │   │   ├── postgre-sql.md
    │   │   │   │   ├── py-charm.md
    │   │   │   │   ├── README.md
    │   │   │   │   ├── stable-diffusion.md
    │   │   │   │   ├── terminal.md
    │   │   │   │   ├── text-embeddings-inference.md
    │   │   │   │   ├── vs-code.md
    │   │   │   │   └── weaviate.md
    │   │   │   ├── pre-installed
    │   │   │   │   ├── jobs
    │   │   │   │   │   ├── README.md
    │   │   │   │   │   ├── remote-debugging-with-pycharm-professional.md
    │   │   │   │   │   └── remote-debugging-with-vs-code.md
    │   │   │   │   ├── buckets.md
    │   │   │   │   ├── disks.md
    │   │   │   │   ├── files.md
    │   │   │   │   ├── flows.md
    │   │   │   │   ├── images.md
    │   │   │   │   ├── README.md
    │   │   │   │   └── secrets.md
    │   │   │   └── README.md
    │   │   └── getting-started
    │   │       ├── clusters.md
    │   │       ├── organizations.md
    │   │       ├── projects.md
    │   │       ├── README.md
    │   │       └── sign-up-login.md
    │   ├── getting-started
    │   │   ├── first-steps
    │   │   │   ├── getting-started.md
    │   │   │   ├── README.md
    │   │   │   ├── running-your-code.md
    │   │   │   └── training-your-first-model.md
    │   │   ├── apolo-base-docker-image.md
    │   │   ├── faq.md
    │   │   ├── references.md
    │   │   └── troubleshooting.md
    │   ├── README.md
    │   └── SUMMARY.md
    └── use-cases
        ├── .gitbook
        │   └── assets
        │       └── Reasoning_Framework.md
        ├── enterprise-ready-generative-ai-applications
        │   ├── apolo-documentation-chatbot.md
        │   └── canada-budget-rag.md
        ├── generic
        │   └── ml-model-lifecycle-on-apolo-platform
        │       ├── end-to-end-ml-model-lifecycle-using-apolo-cli.md
        │       ├── ml-model-lifecycle-using-apolo-console.md
        │       └── README.md
        ├── image-and-video-processing
        │   ├── howto-lora-models-with-stable-diffusion.md
        │   └── synthetic-data-generation-using-stable-diffusion.md
        ├── llms
        │   ├── autonomous-research-with-agentlaboratory-deepseek-r1-vs.-openai-o1.md
        │   ├── deepseek-r1-distilled-models.md
        │   ├── deepseek-r1-model-deployment.md
        │   └── teaching-models-to-reason-training-fine-tuning-and-evaluating-models-with-llama-factory-on-apolo.md
        ├── visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai
        │   ├── architecture-overview.md
        │   ├── implementation.md
        │   └── README.md
        ├── README.md
        └── SUMMARY.md



---
File: /apolo-actions/reference/checkout.md
---

# Checkout

This batch mode action checkouts a repository to the provided volume to make it available in your workflow. By default, it only fetches a single commit.

### Quick example:

```
tasks:
  - id: checkout
    action: gh:apolo-actions/checkout@v1
    args:
      clone_uri: https://github.com/apolo-actions/checkout.git
      checkout_to: "storage:"
      checkout_subpath: dir/to/clone/into
```

### Arguments:

#### `clone_uri`

The URL of the Git repository you want to clone. Both `https://` and `git@` notations are supported.

**Example**

```
args:
  clone_uri: https://github.com/apolo-actions/checkout.git
```

Note that you should provide a `ssh_key_secret` when using the SSH clone notation (`git@...`).

#### `clone_depth`

Number of commits to fetch. `"1"` by default, which means only a single commit will be cloned. To clone the entire repo, set this to `"0"`.

**Example**

```
args:
  clone_depth: "10"
```

#### `ref`

Name of a branch, Git tag, or a commit SHA to fetch. Uses the remote HEAD by default.

**Example**

```
args:
  ref: main
```

#### `ssh_key_secret`

A URI of a [secret](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/secret "mention") that contains an SSH private key to use for cloning.

If you're using a Unix machine with default configuration, you can upload your current private key by using this command:

```
apolo secret add git_ssh_private_key @~/.ssh/id_rsa
```

**Example**

```
args:
  ssh_key_secret: secret:git_ssh_private_key
```

#### `checkout_to`

A URI of a storage folder or disk to use as a volume for checkout. When using a disk, you can specify the directory to checkout via `checkout_subpath`.

Note that the corresponding directory should exist for `storage:` volumes. If you want to automatically create a sub-directory, use `checkout_subpath`.

**Examples**

Storage-based volume

```
args:
  checkout_to: storage:dir/to/checkout
```

Disk-based volume

```
args:
  checkout_to: disk:disk_name_or_id
```

#### `checkout_subpath`

A relative path under `checkout_to` to use as a cloning destination directory. If such folder doesn't exist, it will be automatically created.

**Example**

```
args:
  checkout_subpath: store/repo_content/here
```

#### `erase_subpath`

Enables purging of the directory specified by `checkout_subpath`. Use with caution, as this is the same as running the `rm -rf checkout_subpath` command. To enable this feature, set input to `"true"`.

**Example**

```
args:
  erase_subpath: "true"
```

### Outputs:

#### `head_sha`

A SHA of the commit under the current HEAD in the cloned repository. This output's main goal is to make the action cache-friendly - even if the repository didn't change, that output will be the same and the depending action can safely use the cache.

{% hint style="info" %}
Feel free to check the [Checkout action repository](https://github.com/apolo-actions/checkout).
{% endhint %}



---
File: /apolo-actions/reference/filebrowser.md
---

# Filebrowser

This is an [apolo-flow](https://docs.apolo.us/apolo-flow-reference) action launching the [Filebrowser](https://hub.docker.com/r/filebrowser/filebrowser) app for working with platform storage.

All it needs is a reference to a storage folder that becomes the root folder for the Filebrowser instance.

#### Quick example

```
jobs:
  filebrowser:
    action: gh:apolo-actions/filebrowser@v1.0.1
    args:
      volumes_project_remote: $[[ volumes.project.remote ]]
```

### Arguments

#### `volumes_project_remote`

Reference to the project's remote volume.

#### Example

```
args:
	volumes_project_remote: $[[ volumes.project.remote ]]
```

#### `http_port`

HTTP port to use for Filebrowser. `"80"` by default.

#### Example

```
args:
	http_port: "8888"
```

#### `http_auth`

Whetther to use HTTP authentication for Filebrowser or not. `"True"` by default.

#### Example

```
args:
	http_auth: "False"
```

#### `job_name`

The name of the Filebrowser server. Use it to generate a predictable job hostname. `"filebrowser"` by default.

#### Example

```
args:
	job_name: "browser-job"
```

#### `preset`

Resource preset, used to run the server. The first one in the `apolo config show` list by default.

#### Example

```
args:
	job_name: "browser-job"
```

{% hint style="info" %}
Feel free to check the [Filebrowser action repository](https://github.com/apolo-actions/filebrowser).
{% endhint %}



---
File: /apolo-actions/reference/jupyter.md
---

# Jupyter

This is an [apolo-flow](https://docs.apolo.us/apolo-flow-reference) action launching an instance of [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) or [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/). It's intended to be used with the Apolo [platform template](https://github.com/neuro-inc/cookiecutter-neuro-project), but can be adapted for other use cases as well.

It requires the references to 5 volumes: data, code, config, notebooks and results. These volumes will be mounted to `/project/data`, `/project/modules`, `/project/config`, `/project/notebooks`, and `/project/results` respectively.

By default, this action will use the `ghcr.io/neuro-inc/base:latest` image to run Jupyter.

After the Jupyter instance is launched, its Web UI will be automatically opened in the default browser.

#### Quick example:

```
jobs:
  jupyter:
    action: gh:apolo-actions/jupyter@master
    args:
      volumes_data_remote: ${{ volumes.data.remote }}
      volumes_code_remote: ${{ volumes.code.remote }}
      volumes_config_remote: ${{ volumes.config.remote }}
      volumes_notebooks_remote: ${{ volumes.notebooks.remote }}
      volumes_results_remote: ${{ volumes.results.remote }}
```

### Arguments

#### `volumes_data_remote`

Reference to a data volume

#### Example

```
args:
	volumes_data_remote: ${{ volumes.data.remote }}
```

#### `volumes_code_remote`

Reference to a code volume

#### Example

```
args:
	volumes_code_remote: ${{ volumes.code.remote }}
```

#### `volumes_config_remote`

Reference to a config volume

#### Example

```
args:
	volumes_config_remote: ${{ volumes.config.remote }}
```

#### `volumes_notebooks_remote`

Reference to a notebooks volume

#### Example

```
args:
	volumes_notebooks_remote: ${{ volumes.notebooks.remote }}
```

#### `volumes_results_remote`

Reference to a results volume

#### Example

```
args:
	volumes_results_remote: ${{ volumes.results.remote }}
```

#### `preset`

Resource preset to use when running the Jupyter job. `""` by default.

#### Example

```
args:
    preset: cpu-small
```

#### `jupyter_mode`

The mode in which to run Jupyter - `"notebook"` or `"lab"`. Uses `"notebook"` by default.

#### Example

```
args:
    jupyter_mode: "lab"
```

#### `job_name`

Predictable subdomain name which replaces the job's ID in the full job URI. `""` by default.

#### Example

```
args:
	job_name: "jupyter-job"
```

#### `multi_args`

Additional arguments. `""` by default.

#### `http_port`

HTTP port to use for Jupyter. `"8888"` by default.

#### Example

```
args:
    http_port: "4444"
```

#### `http_auth`

Whether to use HTTP authentication for Jupyter or not. `"True"` by default.

#### Example

```
args:
    http_auth: "False"
```

{% hint style="info" %}
Feel free to check the [Jupyter action repository](https://github.com/apolo-actions/jupyter).
{% endhint %}



---
File: /apolo-actions/reference/remote-debug.md
---

# Remote Debug

This is an [apolo-flow](https://docs.apolo.us/apolo-flow-reference) action enabling remote debugging. It's intended to be used with Apolo [platform template](https://github.com/neuro-inc/cookiecutter-neuro-project), but can be adapted for other use cases as well.

This action exposes SSH port 22 and maps it to port 2211 used for the PyCharm remote Python debugging feature.

It also expects references to 4 remote folders: for data, config, code, and results. These remotes will be mounted to `/project/data`, `/project/config`, `/project/modules` and `/project/results` respectively.

{% hint style="info" %}
Feel free to check the [Remote Debug action repository](https://github.com/apolo-actions/remote_debug).
{% endhint %}



---
File: /apolo-actions/reference/tensorboard.md
---

# Tensorboard

This is an [apolo-flow](https://docs.apolo.us/apolo-flow-reference) action launching a [Tensorboard](https://www.tensorflow.org/tensorboard/) instance.

The only required argument is a reference to a storage folder with your experiment results.

#### Quick example

```
jobs:
  tensorboard:
    action: gh:apolo-actions/tensorboard@master
    args:
      volumes_results_remote: $[[ volumes.results.remote ]]
```

### Arguments

#### `job_name`

Predictable subdomain name which replaces the job's ID in the full job URI. `""` by default

#### Example

```
args:
	job_name: "tensorboard-job"
```

#### `http_port`

HTTP port to use for Tensorboard, `"6006"` by default.

#### Example

```
args:
	http_port: "6666"
```

#### `http_auth`

Whether to use HTTP authentication for Tensorboard. `"True"` by default

#### Example

```
args:
	http_auth: "False"
```

#### `volumes_results_remote`

Reference to a volume with experiment results.

#### Example

```
args:
	volumes_results_remote: $[[ volumes.results.remote ]]
```

{% hint style="info" %}
Feel free to check the [Tensorboard action repository](https://github.com/apolo-actions/tensorboard).
{% endhint %}



---
File: /apolo-actions/reference/vs-code.md
---

# VS Code

This action runs an instance of [VS Code](https://code.visualstudio.com/) and runs in in the default web browser.

It requires the name of the image on which to run VS Code and references to the following 5 volumes: data, code, config, notebooks, and results. These volumes will be mounted to `/project/data`, `/project/modules`, `/project/config`, `/project/notebooks`, and `/project/results` respectively.

#### Quick example

```
jobs:
  vscode:
    action: gh:apolo-actions/vscode@@v1.0.1
    args:
      volumes_data_remote: $[[ volumes.data.remote ]]
      volumes_code_remote: $[[ volumes.code.remote ]]
      volumes_config_remote: $[[ volumes.config.remote ]]
      volumes_notebooks_remote: $[[ volumes.notebooks.remote ]]
      volumes_results_remote: $[[ volumes.results.remote ]]
```

### Arguments

#### `image`

The name of the image on which to run the VS Code instance. Default is `ghcr.io/neuro-inc/base:latest`. If you use an image that's not derived from `ghcr.io/neuro-inc/base`, make sure it has the [VS Code server](https://github.com/cdr/code-server) installed.

#### Example

```
args:
	image: ghcr.io/neuro-inc/base:latest
```

#### `job_name`

Predictable subdomain name that will replace the job's ID in the full job URI. `""` by default

#### Example

```
args:
	job_name: "vscode-job"
```

#### `http_port`

HTTP port to use for VS Code. `"8080"` by default.

#### Example

```
args:
	http_port: 8282
```

#### `http_auth`

Whether to use HTTP authentication for VS Code Web UI or not. `"True"` by default.

#### Example

```
args:
	http_auth: "false"
```

#### `volumes_data_remote`

Reference to a data volume.

#### Example

```
args:
	volumes_data_remote: $[[ volumes.data.remote ]]
```

#### `volumes_code_remote`

Reference to a code volume.

#### Example

```
args:
	volumes_code_remote: $[[ volumes.code.remote ]]
```

#### `volumes_config_remote`

Reference to a config volume.

#### Example

```
args:
	volumes_config_remote: $[[ volumes.config.remote ]]
```

#### `volumes_notebooks_remote`

Reference to a notebooks volume.

#### Example

```
args:
	volumes_notebooks_remote: $[[ volumes.notebooks.remote ]]
```

#### `volumes_results_remote`

Reference to a results volume.

#### Example

```
args:
	volumes_results_remote: $[[ volumes.results.remote ]]
```

{% hint style="info" %}
Feel free to check the [VS Code action repository](https://github.com/apolo-actions/vscode).
{% endhint %}



---
File: /apolo-actions/reference/webdav-server.md
---

# WebDAV Server

With this action, you can serve your data in the Apolo cluster (storage folder, disk, etc.) using [rclone's WebDAV server](https://rclone.org/webdav/).

The only required parameter is the reference to the target remote volume.

#### Quick example

```
jobs:
  webdav_server:
    action: gh:apolo-actions/webdav_server@master
    args:
      volume_remote: ${{ volumes.project.remote }}
```

### Arguments

#### `volume_remote`

Reference to the target volume you want to serve.

#### Example

```
args:
	volume_remote: ${{ volumes.project.remote }}
```

#### `http_auth`

Whether to enable Apolo platform-based authentication or not. If this argument is disabled (set to `""` by default), your WebDAV will not be protected by the Apolo SSO (single sign-on authentication). It has no impact on the `rclone serve webdav` parameters.

#### Example

```
args:
	http_auth: "True"
```

#### `port`

Rclone WebDAV server port. Useful if you want to access the server within the cluster - for instance, from another job. `"8080"` by default.

#### Example

```
args:
	port: "8484"
```

#### `job_name`

The name of the WebDAV server. Use it to generate a predictable job hostname. `"webdav"` by default.

#### Example

```
args:
	job_name: "webdav-job"
```

#### `job_lifespan`

The amount of time for which the WebDAV server job container will be active. `"1d"` by default.

#### Example

```
args:
	job_lifespan: 1d4h20m30s
```

#### `preset`

The resource preset to use when running this job. `"cpu-small"` by default. You can view the list of available presets by running `apolo config show`.

#### Example

```
args:
	preset: "cpu-medium"
```

#### `extra_params`

Extra parameters for the `rclone serve webdav` command.

{% hint style="info" %}
Feel free to check the [WebDAV Server action repository](https://github.com/apolo-actions/webdav_server).
{% endhint %}



---
File: /apolo-actions/README.md
---

# Getting started

In addition to its basic YAML capabilities, [Apolo Flow](https://docs.apolo.us/apolo-flow-reference) allows you to run useful actions to help with the development process.&#x20;

This reference describes each of the actions and their functionality.&#x20;



---
File: /apolo-actions/SUMMARY.md
---

# Table of contents

* [Getting started](README.md)

## Reference

* [Tensorboard](reference/tensorboard.md)
* [Remote Debug](reference/remote-debug.md)
* [Jupyter](reference/jupyter.md)
* [WebDAV Server](reference/webdav-server.md)
* [Filebrowser](reference/filebrowser.md)
* [VS Code](reference/vs-code.md)
* [Checkout](reference/checkout.md)



---
File: /apolo-python-sdk/README.md
---

# The Apolo SDK for Python&#x20;

The Apolo SDK for Python is a comprehensive library designed to facilitate interaction with the Apolo Platform API. It provides developers with tools to manage various platform resources programmatically, including jobs, storage, images, users, secrets, disks, service accounts, and buckets.

[Link to full Apolo SDK documentation](https://apolo-sdk.readthedocs.io/latest/index.html)

### **Key Features:**

* **Jobs Management**: Submit, monitor, and control jobs within the Apolo Platform.
* **Storage Operations**: Handle file uploads, downloads, and manage storage resources.
* **Image Handling**: Manage container images, including pulling and pushing images to the Apolo registry.
* **User and Access Control**: Manage user information and permissions.
* **Secrets Management**: Securely store and retrieve sensitive information.
* **Disk Management**: Create and manage persistent storage disks.
* **Service Accounts and Buckets**: Manage service accounts and cloud storage buckets.

### **Installation:**

The SDK can be installed via pip:

`pip install -U apolo-sdk`

### **Getting Started:**

To begin using the SDK, authenticate with the Apolo Platform using the CLI:

`apolo login`

After authentication, initialize the client in your Python code:

```python
import apolo_sdk
async with apolo_sdk.get() as client:
async with client.jobs.list() as job_iter:
jobs = [job async for job in job_iter]
```

This example demonstrates how to instantiate a client and retrieve a list of jobs.

### **Documentation Structure:**

The documentation is organized into the following sections:

* **Usage**: Provides practical examples and guides on using the SDK for various tasks.
* **Reference**: Offers detailed API references for all classes, functions, and modules within the SDK.

For more information, visit the [Apolo SDK documentation](https://apolo-sdk.readthedocs.io/latest/index.html).



---
File: /apolo-python-sdk/SUMMARY.md
---

# Table of contents

* [The Apolo SDK for Python ](README.md)



---
File: /docs/administration/cluster-management/creating-a-cluster.md
---

# Creating a Cluster

### Introduction

Apolo lets you create a cluster in any of the three major cloud providers - [Amazon Web Services](https://aws.amazon.com/), [Google Cloud Platform](https://cloud.google.com/), and [Azure](https://azure.microsoft.com/en-in/). After you sign up with a cloud provider, you have to share your service account information and the configuration you need with our team. We will then set up a cluster on your behalf, and install Apolo on your cloud for you.

To set up a Apolo cluster, you have to do the following:

1. Set up a cloud environment:
   * GCP: [Create a project](https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project) and a [service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating).
   * AWS: [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html#getting-started-create-vpc) and a [service account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).
   * Azure: [Create a resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups) and a [service account](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).
2. Prepare a cluster configuration YAML file.
3. Share the configuration YAML file with us. Once we receive the YAML file, we will set up and run the cluster (usually completed within one business day). You can start [adding your users to the cluster](managing-users-and-quotas.md) while it is being set up.

Apart from the process mentioned above, there are other methods of setup:

* Set up Apolo on an existing cluster provided by AWS, GCP, or Azure. This requires the configuration of the node pool.&#x20;
* Set up Apolo on an existing cluster provided by other cloud service providers.
* Set up Apolo on-premise (or “bare metal”).

For any of these other methods of setup, please [contact our team](mailto:support@apolo.us).

### Cluster configuration YAML&#x20;

You must create a project/VPC/resource group and a service account with all required permissions before you can start preparing a cluster configuration YAML file. The YAML file is used by the Apolo team to set up and run the cluster. You should use the `apolo admin generate-cluster-config` command to generate the YAML file. It is an interactive tool that generates a valid configuration file with the default node configuration based on your responses.

The command prompts for the following information in order to generate the configuration file:

| **Prompt**                                                                                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cluster Type                                                                                       | Enter cloud service provider - AWS, GCP, Azure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| GCP Project Name or AWS VPC ID or Azure subscription ID                                            | <ul><li>For GCP, enter the name of the project.</li><li>For AWS, enter the VPC ID you created in the previous step.</li><li>For Azure, enter the Azure subscription ID you created in the previous step.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <p>Service Account Key File (.json)</p><p>Or</p><p>AWS Profile Name</p><p>Or Azure information</p> | <ul><li>For GCP, enter the path to the service account key file. For information on service accounts, see <a href="https://cloud.google.com/iam/docs/understanding-service-accounts">Understanding service accounts</a>.</li><li>For AWS, enter the profile name in AWS. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html">Managing Access Keys</a>.</li><li><p>For Azure, enter the following access information:</p><ul><li><a href="https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#create-a-new-application-secret">Azure client ID</a></li><li><a href="https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#create-a-new-application-secret">Azure tenant ID</a></li><li><a href="https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#create-a-new-application-secret">Azure client secret</a></li><li><a href="https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#assign-a-role-to-the-application">Azure resource group</a></li><li>Azure Files storage size (GB)</li></ul></li></ul> |

Below is a sample command for GCP:

```
> apolo admin generate-cluster-config
Select cluster type (aws, gcp, azure): gcp
GCP project name: My Project
Service Account Key File (.json): GCP_User.json
Cluster config cluster.yml is generated.
```

The command creates the `cluster.yml` file that includes the information required by the Apolo team to set up your cluster. Here is a sample `cluster.yml` generated for a new GCP cluster:

```
type: gcp
location_type: multi_zonal
region: us-central1
zones:
- us-central1-a
- us-central1-c
project: My Project
credentials:
 auth_provider_x509_cert_url: https://www.googleapis.com/oauth2/v1/certs
 auth_uri: https://accounts.google.com/o/oauth2/auth
 client_email: johndoe@intricate-web-236410.iam.gserviceaccount.com
 client_id: '105087309181394151560'
 client_x509_cert_url: https://www.googleapis.com/robot/v1/metadata/x509/johndoe%40intricate-web-236410.iam.gserviceaccount.com
 private_key: ...
 private_key_id: ...
 project_id: intricate-web-236410
 token_uri: https://oauth2.googleapis.com/token
 type: service_account
node_pools:
- id: n1_highmem_8
 min_size: 1
 max_size: 4
- id: n1_highmem_8_1x_nvidia_tesla_k80
 min_size: 1
 max_size: 4
- id: n1_highmem_8_1x_nvidia_tesla_v100
 min_size: 0
 max_size: 1
storage:
 id: standard
 capacity_tb: 4
```

The file contains a default nodes pools configuration that is used as a starting point:

* 1 non-preemptive node with K80
* 1 non-preemptive node with V100
* 4 non-preemptive non-GPU nodes
* and 4 Tb of standard storage

The file will create a cluster with the following presets:

* cpu-small,
* cpu-large,
* gpu-small (a node with K80), and
* gpu-large (a node with V100).

To get information about available options for each of the cloud providers, run:

`apolo admin show-cluster-options` .

You can further update the `cluster.yml` file as per your requirements before you send it to us. If you have any issues updating the file, then [contact us](mailto:support@apolo.us). Once you are done updating the configuration file, you should send the cluster.yml file to the Apolo team for the cluster setup using the command:

`apolo admin add-cluster <path/to/config>`

Once we receive the YAML file, we will set up and run the cluster (usually completed within one business day). After the command is run, you become the admin of the cluster. You can start adding users to the cluster as soon as you run the command above.



---
File: /docs/administration/cluster-management/creating-node-pools.md
---

# Creating Node Pools

### Node Pools in AWS, GCP, and Azure

As explained in the [Creating a Cluster](creating-a-cluster.md) topic, when you're creating a new platform cluster in [Amazon Web Services](https://aws.amazon.com/), [Google Cloud Platform](https://cloud.google.com/), or [Azure](https://azure.microsoft.com/en-in/), the default node pool setup that will be used as a starting point for the new cluster is determined by the cluster configuration file created by running `apolo admin generate-cluster-config`

You can check the default node pool setup in the **node\_pools** section of the `cluster.yml` file:

```
node_pools:
- id: n1_highmem_8
 min_size: 1
 max_size: 4
- id: n1_highmem_8_1x_nvidia_tesla_k80
 min_size: 1
 max_size: 4
- id: n1_highmem_8_1x_nvidia_tesla_v100
 min_size: 0
 max_size: 1
storage:
 id: standard
 capacity_tb: 4
```

Once the cluster is created and set up by our team, a more detailed information about your cluster's node pools can be viewed by running the `apolo admin get-clusters` command in CLI:

```
> apolo admin get-clusters
company-cluster                                                                                      
 Status      Deployed                                                                              
 Cloud       azure                                                                                 
 Region      eastus                                                                                
 Zones       2                                                                                     
 Node pools                                                                                        
               Machine            CPU   Memory   Preemptible                     GPU   Min   Max   
              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
               Standard_D8_v3     7.0    28.0G        ×                                  1    10   
               Standard_NC6       5.0    50.0G        ×         1 x nvidia-tesla-k80     0    30   
               Standard_NC6       5.0    50.0G        √         1 x nvidia-tesla-k80     0    30   
               Standard_NC6s_v3   5.0   106.0G        ×        1 x nvidia-tesla-v100     0    10   
               Standard_NC6s_v3   5.0   106.0G        √        1 x nvidia-tesla-v100     0    10   
                                                                                                   
 Storage     Premium tier Azure Files with LRS replication type and 3072 GiB file share size  
```

If you need to change the your node pools, please contact our team at [support@apolo.us](mailto:support@apolo.us)

### Node Pools in an On-premise Installation

If you prefer to create an on-premise platform cluster, node pools are set up in a more individualized way from the start.

Once the set of machines required for your cluster is agreed upon, all of these machines will be grouped by their operating characteristics. Machines with identical characteristics will be combined into node pools and then given labels based on what node pool they are a part of.&#x20;

If a need to add a new machine to any of the existing node pools arises, this new machine will have to share the characteristics with other machines of the target node pool. It will also be labeled respectively to make sure it's readable and accessible as a part of this node pool. &#x20;

### Next Steps

Once the node pools are set up, you can start [configuring your cluster's usable presets](managing-presets.md). This will help create an environment streamlined specifically for your development and deployment workflow.



---
File: /docs/administration/cluster-management/managing-organizations.md
---

# Managing organizations

Organizations provide an additional way to group users.

An organization represents a group of people with roles. In this way, it's similar to a cluster, but there are no computational resources behind an organization.

Also, all organization users (including its manager/admin) will use a shared total quota that was set for this specific organization in the cluster.

### Creating organizations

You can create a new organization by using the `apolo admin add-org` command:

```
$ apolo admin add-org my-org
```

After this, you can add users to it with the `apolo admin add-org-user` command:

```
$ apolo admin add-org-user my-org alice user
```

Next, an admin or manager of the cluster can add the new organization to the cluster via the `apolo admin add-org-cluster` command, and then assign quotas within the organization:

```
$ apolo admin add-org-cluster my-cluster my-org
```

Organization managers and admins will have access to all of the resources and users from their organization, but no access to the resources of other organizations or users that aren't members of any organization.

### Assigning managers/admins

An organization will need its own manager or admin who will be able to add new members from this point ion. To assign a cluster's user as an organization admin, use the following command:

```
$ apolo admin add-cluster-user --org ORGANIZATION_NAME CLUSTER_NAME USER_NAME admin
```

An organization manager or admin differs from a cluster manager or admin in that they cannot add people _not on behalf of the organization_ (without the --org parameter).

### Switching organizations

Since a user can be added to the same cluster on behalf of several organizations (as well as directly), it is possible to switch the current organization by using the `apolo config switch-org` command, similarly to how you would switch the current cluster. When an organization is selected, all jobs, files, secrets, disks, etc., will be created within this organization.\
This means that the respective URIs will have the following structure:

```
schema://cluster/organization/username/some/path
```

{% hint style="info" %}
You can find more information about organization-related CLI commands in the [corresponding section of our CLI Reference.](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/admin#add-org)
{% endhint %}



---
File: /docs/administration/cluster-management/managing-presets.md
---

# Managing Presets

Once your cluster's node pools are set up, you can configure resource presets that will be available for you and your team during the work process. This can be done both through the CLI and in the Apolo Console.

{% tabs %}
{% tab title="CLI" %}
**Checking your cluster's presets**

You can view your current cluster's resource presets by running `apolo config show` and referring to the **Resource Presets** section in its output:

```
Name               #CPU   Memory   Round Robin   Preemptible Node   GPU                             Jobs Avail   Credits per hour 

 cpu-small             1     4.0G                                                                          20   10               
 cpu-large             4    10.0G                                                                           8   10               
 gpu-small            23    60.0G                                  1 x nvidia-geforce-rtx-2080ti            1   10               
 gpu-large            47   120.0G                                  2 x nvidia-geforce-rtx-2080ti            0   10               
 gpu-1x3090           23    60.0G                                  1 x nvidia-geforce-rtx-3090              0   10               
 gpu-2x3090           47   120.0G                                  2 x nvidia-geforce-rtx-3090              0   10               
 cpu-medium            2     6.0G                                                                          13   10               
 cpu-micro           0.1     1.0G                                                                          83   5                
 cpu-test-storage    7.0    30.0G                                                                           2   75
```

**Modifying and adding presets**

You can easily modify or add resource presets by using the `apolo admin update-resource-preset` command.

For example, to change the amount of memory accessible through the existing **cpu-large** preset to 32GB, run:

```bash
> apolo admin update-resource-preset -m 32G company-cluster cpu-large
```

To add a new preset, just provide its name and parameters in the `apolo admin update-resource-preset` command. You can learn more about using this command [here](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/admin#update-resource-preset).

**Deleting presets**

You can delete resource presets by using the `apolo admin remove-resource-preset` command. For example:

```bash
> apolo admin remove-resource-preset company-cluster cpu-medium
```
{% endtab %}

{% tab title="Apolo Console" %}
**Checking your cluster's presets**

You can view your current cluster's resource presets in the **Information** and **Cluster management** tabs:

![](../../.gitbook/assets/image%20\(116\).png)

**Adding presets**

To add a new preset, click the **Add** icon in the Cluster management tab:

![](../../.gitbook/assets/image%20\(121\).png)

After that, enter the desired preset parameters and click the **Save** icon:

![](../../.gitbook/assets/image%20\(122\).png)

**Modifying presets**

To modify an existing preset, click the **Edit** icon next to it:

![](../../.gitbook/assets/image%20\(118\).png)

After that, enter the new parameters and click the **Save** icon:

![](../../.gitbook/assets/image%20\(117\).png)

**Deleting presets**

To delete a preset, click the **Delete** icon next to it:

![](../../.gitbook/assets/image%20\(119\).png)

After that, click the **Save** icon to confirm your action:

![](../../.gitbook/assets/image%20\(120\).png)
{% endtab %}
{% endtabs %}

###



---
File: /docs/administration/cluster-management/managing-users-and-quotas.md
---

# Managing Users and Quotas

Apolo creates a cluster based on the cluster configuration file you send to our team. The user who creates the cluster is designated the admin of the cluster. You must add users and, optionally, quotas before you can start using the nodes in the cluster. You can know the list of clusters that you can manage by running the `apolo admin get-clusters` command.

```
> apolo admin get-clusters
company-cluster                                                                                      
 Status      Deployed                                                                              
 Cloud       azure                                                                                 
 Region      eastus                                                                                
 Zones       2                                                                                     
 Node pools                                                                                        
               Machine            CPU   Memory   Preemptible                     GPU   Min   Max   
              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
               Standard_D8_v3     7.0    28.0G        ×                                  1    10   
               Standard_NC6       5.0    50.0G        ×         1 x nvidia-tesla-k80     0    30   
               Standard_NC6       5.0    50.0G        √         1 x nvidia-tesla-k80     0    30   
               Standard_NC6s_v3   5.0   106.0G        ×        1 x nvidia-tesla-v100     0    10   
               Standard_NC6s_v3   5.0   106.0G        √        1 x nvidia-tesla-v100     0    10   
                                                                                                   
 Storage     Premium tier Azure Files with LRS replication type and 3072 GiB file share size       

```

You can know the list of clusters that you can access by running the `apolo config get-clusters` command.

You can manage users and user quotas from the CLI. The next sections discuss how you can manage users and user quotas.

### What are the different roles available?

Apolo provides three predefined roles that you can assign to a user - `user`, `manager`, `admin`. The default role is User. The following table describes what each of the roles can do. Please note that any registered platform user may create new clusters; upon creation, a user automatically gets an Admin role in it.

| **Role** | **Description**                                                                                                                      | **Privileges**                                                                                                                                              |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User     | The general users of the platform without special privileges. These users can manage their own and shared jobs, storage, and images. | <ul><li>Manage own and shared jobs</li><li>Manage own and shared storage</li><li>Manage own and shared images</li></ul>                                     |
| Manager  | The users who can manage all jobs, storage, and images on the cluster, as well as manage other users.                                | <ul><li>Manage all cluster jobs</li><li>Manage all cluster storage</li><li>Manage all cluster images</li><li>Manage users</li></ul>                         |
| Admin    | The same as Manager, but additionally they can change cluster configuration or remove clusters. The admins can also add node pools.  | <ul><li>Manage all cluster jobs</li><li>Manage all cluster storage</li><li>Manage all cluster images</li><li>Manage users</li><li>Remove clusters</li></ul> |

### How to add a user to a cluster?

You can add any number of users to a cluster. However, before adding a user you must decide on the role and the quota that you want to set for the user.

The role determines the access rights a user will have on the platform. The quota determines the number of GPU or CPU hours a user can use.

```
> apolo admin add-cluster-user neuro-public john user
Added john to cluster default as user
```

### How to remove a user from the cluster?

You can remove a user from the cluster if you are an Admin or Manager. You must use the `apolo admin remove-cluster-user` command to remove the user. By doing this, you revoke the user’s access to the cluster. All the entities belonging to the user are left (storage, jobs, images, etc), and you can add this user back later.

```
> apolo admin remove-cluster-user default john
Removed john from cluster default
```

### How to promote/demote a user?

You need to remove a user from a given cluster and to add them again with the desired role. All the entities belonging to the user (storage, jobs, images, etc) are not affected during removal.

### How to manage a user’s quota?

The quota determines the amount of GPU or CPU computation accessible to a user. By default, a user is given a quota of 100 credits.

You can set a user’s quota by using one of these commands:

* `apolo admin set-user-quota -c` : Use this to set the quota to a certain number of credits.

```
> apolo admin set-user-quota -c 200 default john
```

* `apolo admin add-user-quota`: Use this to add a certain number of credits to the existing user quota.

```
> apolo admin add-user-quota -c 50 default john
```

You can also set an unlimited quota for a user:

```
> apolo admin set-user-quota default john
```

You can check the quota of any user of a cluster if you are a manager or an admin of the cluster.

```
> apolo config show-quota john
```

To view your own quota, run:

```
> apolo config show-quota
```



---
File: /docs/administration/cluster-management/README.md
---

# Cluster Management

This group contains the following topics:

{% content-ref url="creating-a-cluster.md" %}
[creating-a-cluster.md](creating-a-cluster.md)
{% endcontent-ref %}

{% content-ref url="managing-users-and-quotas.md" %}
[managing-users-and-quotas.md](managing-users-and-quotas.md)
{% endcontent-ref %}

{% content-ref url="creating-node-pools.md" %}
[creating-node-pools.md](creating-node-pools.md)
{% endcontent-ref %}

{% content-ref url="managing-presets.md" %}
[managing-presets.md](managing-presets.md)
{% endcontent-ref %}

{% content-ref url="reports.md" %}
[reports.md](reports.md)
{% endcontent-ref %}




---
File: /docs/administration/cluster-management/reports.md
---

# Reports

The **Information** tab contains widgets for accessing cluster-wide data reports which can help you get a clearer picture of how your cluster is operating and find any issues if there are any.

The **reports** functionality is based on [Grafana](https://grafana.com), an open-source analytics and interactive visualization web service. Feel free to refer to their [documentation](https://grafana.com/docs/grafana/latest/?utm_source=grafana_footer) to learn more about Grafana's functionality.

## Types of reports

There are three types of cluster-wide reports you can access:

* Cluster nodes monitor
* Cluster jobs monitor
* Cluster prices monitor

Let's look at each one of them more closely.

### Cluster nodes monitor

This report provides in-depth information about the activity of the cluster's nodes, including their uptime, CPU and RAM usage, system processes, network traffic, and much more.

You can access it by clicking **CLUSTER NODES MONITOR** on the **Cluster management** tab:

<div align="left"><img src="../../.gitbook/assets/image (237).png" alt=""></div>

The **Nodes** section provides a quick overview of the cluster's nodes:&#x20;

![](<../../.gitbook/assets/image (160).png>)

Clicking a node's name in the **Nodes** section will make it active, allowing you to see detailed information about it in the sections below:

![](<../../.gitbook/assets/image (163).png>)

You can expand any specific section by clicking it's name:

![](<../../.gitbook/assets/image (170).png>)

### Cluster jobs monitor

This report provides a thorough look at the cluster's jobs and their activity, including the jobs' owners, IDs, start times, CPU and memory usage, and more.&#x20;

You can access it by clicking **CLUSTER JOBS MONITOR** in the **Cluster management** tab:

<div align="left"><img src="../../.gitbook/assets/image (242) (1).png" alt=""></div>

The **Running Jobs** widget gives an overview of all currently running jobs, including the information about resource consumption:

![](<../../.gitbook/assets/image (164).png>)

You can view the amount of jobs per user in the **Number of Jobs** and **Total Number of Jobs** widgets:

![](<../../.gitbook/assets/image (155).png>)

Additional sections with information can be expanded by clicking their names:

![](<../../.gitbook/assets/image (145).png>)

Clicking a job's name will bring you to a page with detailed information about this specific job:

![](<../../.gitbook/assets/image (146).png>)

### Cluster prices monitor

This report provides information related to cluster pricing, such as node costs, job credit use, job duration, and more.

You can access this report by clicking **CLUSTER PRICES MONITOR** in the **Cluster management** tab:

<div align="left"><img src="../../.gitbook/assets/image (251).png" alt=""></div>

The uppermost section displays total job credits used in the selected time range, job duration, total cost of available nodes, and the uptime of these nodes. The **Jobs** widget shows a rundown of the jobs - their IDs, owners, presets, start times, and credit costs:

![](<../../.gitbook/assets/image (151).png>)

The lowermost widgets show more information about users and nodes:

![](<../../.gitbook/assets/image (161).png>)

## Report time ranges and refresh time

Each report has a default time range for which it's generated, based on the report's type. You can specify any other range in the **Time range** drop-down tab:

![](<../../.gitbook/assets/image (153).png>)

You can also choose how often the report refreshes in the **Refresh rate** drop-down list:

![](<../../.gitbook/assets/image (156).png>)



---
File: /docs/administration/overview-and-installation/architecture-overview.md
---

# Architecture Overview

Apolo is an MLOps PaaS that facilitates and supports the full cycle of ML operations such as data processing, model development, training, and deployment.

### High-level Architecture

Apolo consists of multiple logical parts:

* The **Control Plane**, dedicated to managing all aspects of the platform;
  * **The CLI**;
  * **The Web Application**;
* A **Compute Cluster**, a first-class citizen within the Control Plane, dedicated to running ML workloads;

### Control Plane

The Control Plane is the brains of the platform. Its responsibilities include, but are not limited to:

* Managing users and their resource quotas;
* Managing RBAC/ACL;
* Managing Compute Clusters and their lifecycle;
* Storing the metadata of jobs;
* Managing the lifecycle of jobs;
* Sending user notifications;
* Hosting the Web Application;
* Hosting the Web Documentation;

The Control Plane requires:

* A load balancer with an external IP address;
* Kubernetes for running a fleet of management microservices;
  * A properly configured default StorageClass;
  * Traefik as the Ingress Controller;
* PostgreSQL for storing job metadata, user metadata, and roles;
* Redis for storing the ACLs of roles and queueing user notifications;

#### Components

**Auth API**

A typical extensible API for managing and enforcing hierarchical access control lists (ACLs) that are bound to roles.

**Admin API**

A high-level semantic API on top of the Auth API for managing users, clusters they have access to, roles they take in these clusters, their quotas within the clusters, etc.

**Config API**

An API for managing the lifecycle of clusters. This API allows cluster provisioning, changing cluster configuration, cluster decommissioning, etc. It uses Argo Workflows and Terraform under the hood.

**Jobs API**

An API for storing the metadata of jobs, managing their lifecycle, and enforcing user quotas. This service connects to the Kubernetes APIs of the clusters.

**Ingress Auth**

A service that enforces the optional single sign-on authentication scheme for jobs that expose an HTTP port. This also implements the forward authentication strategy for the Traefik Ingress Controller.

**Notifications API**

An API for sending email/Slack notifications for events such as job status transitions, user quota depletion, etc.

**Apps API**

An API for running a curated set of applications from within the Apolo Console.\\

![](</docs/.gitbook/assets/neu.ro-architecture-overview (1) (1).png>)

**Apolo Console**

A Apolo Console for managing compute workloads, running applications, managing secrets, checking user quotas, etc.

**Apolo CLI**

The main tool for interacting with both the control plane and compute clusters. Enables users to manage clusters and switch between them, manage compute workloads, manage storage and container images, etc

**Apolo-Flow CLI**

An engine for running computational workflows based on Apolo CLI and SDK .

**Apolo-Extras CLI**

A collection of useful tools based on Apolo CLI and SDK, e.g., transfer of storage and container images between clusters.\\

**Web Documentation**

An up-to-date user documentation for the Apolo Console and CLIs with usage examples and other useful information.\\

![](</docs/.gitbook/assets/neu.ro-architecture-overview-2 (1).png>)

### Compute Cluster

A typical compute cluster requires:

* A load balancer with an external IP address;
* A Kubernetes cluster for running a fleet of controlling microservices as well as compute workloads;
* A container registry, either managed by a cloud provider or running within the Kubernetes cluster;
* A low-latency high-throughput network file storage accessible via NFS/SMB;
* A cost-efficient object storage for archival purposes;

#### Components

**Storage API**

An API for managing the contents of the network file storage.

**Blob Storage API**

An API for managing buckets and objects in the object storage.

**Registry API**

A Docker-Registry-API-compatible service for managing container images.

**Monitoring API**

An API for streaming real-time and historical logs and real-time telemetry of compute workloads, as well as allowing remote command execution and port forwarding.

**Secrets API**

An API for managing user secrets.

**Disk API**

An API for managing persistent block storage.

**Reports**

A service for retrieving historical telemetry of compute workloads with respect to user permissions.\\

![](<../../.gitbook/assets/neu.ro-architecture-overview-3 (1).png>)



---
File: /docs/administration/overview-and-installation/on-premise-installation-guide.md
---

# On-premise Installation Guide

### Requirements:

* Kubernetes cluster:
  * It must be able to use **OpenEBS Cstor**. Disks have to be attached to Kubernetes nodes and must not be mounted or formatted.
  * If there is no internet access, each node should have a **busybox:latest** image preloaded.
* A linux VM:
  * Must be accessible by the Kubernetes cluster (this VM will host the docker registry along with the **chartmuseum** and **devpi** services, which are needed to run the platform).
  * Must have access to the Kubernetes cluster.
  * The following utilities have to be installed: **docker, kubectl, jq.**

### Archive Structure

**/chartmuseum**

* A directory with all required helm charts. It will be mounted as a volume to the **chartmuseum** container.

**/registry**

* A directory with all required docker images. It will be mounted as a volume to the **registry** container.

**/devpi**

* A directory with the **apolo-cli** python package and all its dependencies. It will be mounted as a volume to the **devpi** container.

**registry.tar**

* Saved **registry:2** image.

**chartmuseum.tar**

* Saved **chartmuseum/chartmuseum:latest** image.

**devpi.tar**

* Saved **devpi** image.

**jq.tar**

* Saved **imega/jq:latest** image, command-line JSON processor.

**yq.tar**

* Saved **mikefarah/yq:latest** image, command-line YAML processor.

**k8s/\*.yaml**

* Kubernetes resources that will be created in the cluster.

**\*.sh**

* Installation scripts.

### Platform Setup

Connect to the Linux VM and ensure that **kubectl** can connect to the Kubernetes cluster:

```
kubectl get nodes
```

Mount the USB (or external storage) device and extract the **apolo.tar** archive:

```
mkdir –p $HOME/apolo
tar -xvf apolo.tar -C $HOME/apolo
```

Prepare the config file (see [example below](on-premise-installation-guide.md#config-file-example)), run the installation script, and wait until all pods are in the Running state:

```
$HOME/apolo/install.sh $CONFIG_FILE_PATH
```

By default, if there is no Ingress certificate specified in the config file, the installation script will generate a self-signed certificate. This self-signed certificate has to be added to the certificate trust store in the platform user's development environment.

#### Configure the DNS Server

Set up A records to the platform domains **\*.neu.ro**, **default.org.neu.ro**, **\*.default.org.neu.ro**, **\*.jobs.default.org.neu.ro** in such a way that they point to all Kubernetes cluster IPv4 addresses.

### Config File Example

```
 server:
  ip: "10.240.0.8"
ui:
  type: minzdrav
ingress_ssl:
  cert_path: "/path/to/ingress.crt" # optional
  cert_key_path: "/path/to/ingress.key" # optional
postgres:
  password: changeme
  size: 10Gi
redis:
  password: changeme
  size: 10Gi
keycloak:
  username: admin
  password: changeme
auth:
  jwt_secret: changeme
registry:
  size: 10Gi
storage:
  size: 10Gi
blob_storage:
  size: 10Gi
metrics:
  size: 10Gi
node_pools:
- name: cpu
  cpu: 8
  memory_gb: 6
  disk_size_gb: 6
  nodes:
  - aks-agentpool-36699122-vmss000002
- name: gpu
  cpu: 8
  memory_gb: 6
  disk_size_gb: 6
  gpu: 1
  gpu_model: nvidia-tesla-k80
  nodes:
  - aks-agentpool-36699122-vmss000002
```

### Development Environment Setup

#### Add the certificate to the trust store (in case a self-signed certificate was generated during setup)

* Download the Ingress certificate:

```
openssl s_client -connect app.neu.ro:443 -showcerts </dev/null > ingress.crt
```

* Add it to your machine's trust store.

#### Install **Apolo** CLI

Run the following command to install Apolo CLI:

```
pip install -i http://$SERVER_IP/root/pypi apolo-cli
```



---
File: /docs/administration/overview-and-installation/README.md
---

---
hidden: true
---

# Overview and Installation

This group contains the following topics:

{% content-ref url="architecture-overview.md" %}
[architecture-overview.md](architecture-overview.md)
{% endcontent-ref %}

{% content-ref url="on-premise-installation-guide.md" %}
[on-premise-installation-guide.md](on-premise-installation-guide.md)
{% endcontent-ref %}




---
File: /docs/apolo-concepts-cli/apps/files.md
---

# Files

## Overview

The Files application is a comprehensive file management system designed to help you organize and manage your network storage within the cluster. This documentation will guide you through its features and functionality using Apolo CLI. To learn more about the Files app and how you can use it in Apolo Console, visit the main [Files app](../../apolo-console/apps/pre-installed/files.md) page.

## **Command Line Interface (CLI)**

In addition to the graphical interface, you can manage your storage through our powerful command-line interface (CLI). The CLI provides advanced capabilities for file operations, particularly useful for automation and bulk operations.

### Managing Storage

Through the command line, you can perform all essential file operations using the `apolo storage` command set. Here are some key capabilities:

The CLI supports essential operations such as copying files (`cp`), creating directories (`mkdir`), moving files (`mv`), and removing files (`rm`). It also provides advanced features like storage usage analysis (`df`) and tree-style directory visualization (`tree`). When working with files programmatically or handling batch operations, the CLI offers precise control and automation capabilities.

For example, you can copy files to your storage using:

```bash
apolo storage cp local_file.txt storage:
```

Or list your storage contents in a tree format:

```bash
apolo storage tree
```

The CLI is particularly valuable for:

* Automating file operations in scripts
* Performing bulk file transfers
* Integration with development workflows
* Remote storage management
* Pattern-based file operations using glob patterns

For comprehensive documentation of all CLI commands and their options, please refer to our detailed [CLI documentation for storage](https://docs.apolo.us/index/apolo-cli/commands/storage).

### **Mounting Storage in Jobs**

When running computational jobs, you often need to access files from your storage. The Files system integrates seamlessly with our job execution system, allowing you to mount directories from your storage as volumes inside your containers. This gives your jobs direct access to your files, making it easy to process data and save results.

**How Storage Mounting Works**

When you mount a storage volume, you create a connection between a directory in your storage and a location inside your job's container. Think of it like creating a window between your storage and your running job - any files in the mounted storage directory become accessible from within your job.

You can mount volumes in two modes:

1. Read-write mode (`rw`): Allows your job to both read existing files and write new ones
2. Read-only mode (`ro`): Provides access to read files but prevents modifications

**Mounting Volumes Using the CLI**

To mount a volume when running a job, use the `--volume` (or `-v`) option with the `apolo job run` command (see [Apolo CLI reference ](https://docs.apolo.us/index/apolo-cli/commands/job#run)for more information on running jobs). The volume specification follows this format:

```bash
--volume=storage:<source-path>:<container-path>:<mode>
```

Where:

* `<source-path>`: The path in your storage (relative to your project root)
* `<container-path>`: Where the files will appear inside the container
* `<mode>`: Either `ro` (read-only) or `rw` (read-write)

For example, to mount your project's data directory in read-only mode:

```bash
apolo job run --volume=storage:/data:/workspace/data:ro python:3.9
```

You can mount multiple volumes in the same job:

```bash
apolo job run \
    --volume=storage:/input:/workspace/input:ro \
    --volume=storage:/output:/workspace/output:rw \
    pytorch/pytorch:latest
```

### **Using Storage in Workflows**

Workflows provide powerful capabilities for integrating your storage with computational jobs. Let's explore how to effectively use storage volumes in your workflow definitions.

**Understanding Volumes in Workflows**

Volumes in workflows create a three-way connection between:

1. Your local development environment
2. Your storage in the Apolo platform
3. The running jobs in your workflows

This three-way connection enables seamless data flow between development, storage, and computation. Let's look at how to define and use volumes in your workflow configuration.

**Defining Volumes**

In your workflow YAML file, you can define volumes in two ways:

1. **Direct Reference** - Specify the volume directly where it's needed:

```yaml
jobs:
  train_model:
    image: pytorch/pytorch:latest
    volumes:
      - storage:/data:/workspace/data:ro  # Direct reference
```

2. **Volume Definitions** - Define volumes centrally and reference them throughout:

```yaml
volumes:
  training_data:
    remote: storage:/data
    mount: /workspace/data
    local: ./data
    read_only: true

jobs:
  train_model:
    image: pytorch/pytorch:latest
    volumes:
      - ${{ volumes.training_data.ref }}
```

The second approach offers several advantages:

* Centralized volume management
* Reusability across multiple jobs
* Easier synchronization between local and remote storage

**Common Volume Patterns**

Here are some effective patterns for organizing your workflows with volumes:

1. **Input/Output Separation**:

```yaml
volumes:
  input_data:
    remote: storage:/data/input
    mount: /workspace/input
    read_only: true
  
  output_data:
    remote: storage:/data/output
    mount: /workspace/output

jobs:
  process_data:
    image: python:3.9
    volumes:
      - ${{ volumes.input_data.ref }}
      - ${{ volumes.output_data.ref }}
```

2. **Development Environment**:

```yaml
volumes:
  code:
    remote: storage:/src
    mount: /workspace/src
    local: ./src
  
  config:
    remote: storage:/config
    mount: /workspace/config
    local: ./config

jobs:
  develop:
    image: python:3.9
    volumes:
      - ${{ volumes.code.ref }}
      - ${{ volumes.config.ref }}
```

**Volume Synchronization**

When you define a volume with a `local` path, you can synchronize it with your storage using the CLI:

```bash
# Upload local changes to storage
apolo-flow upload

# Download storage changes locally
apolo-flow download
```

This is particularly useful for development workflows where you need to:

* Push code changes to a development environment
* Download computation results
* Share data between team members

**Best Practices**

1. **Use Read-Only Volumes for Input**: Protect your source data by mounting input volumes as read-only:

```yaml
volumes:
  dataset:
    remote: storage:/datasets/imagenet
    mount: /data
    read_only: true
```

2. **Organize Volumes by Purpose**: Structure your volumes based on their role:

```yaml
volumes:
  # Development volumes
  source_code:
    remote: storage:/src
    mount: /app/src
    local: ./src

  # Data volumes
  training_data:
    remote: storage:/data/train
    mount: /data/train
    
  # Output volumes
  model_artifacts:
    remote: storage:/models
    mount: /artifacts
```

3. **Use Volume References**: When the same volume is used in multiple jobs, define it once and reference it:

```yaml
jobs:
  train:
    volumes:
      - ${{ volumes.training_data.ref }}
  
  evaluate:
    volumes:
      - ${{ volumes.training_data.ref }}
```

For complete details on volume configuration options and advanced usage, refer to our [workflow syntax documentation](https://docs.apolo.us/index/apolo-flow-reference/workflow-syntax/live-workflow-syntax) and [Apolo Flow CLI reference](https://docs.apolo.us/index/apolo-flow-reference/cli).

### **Managing Data Transfers with apolo-extras**

The `apolo-extras` CLI provides powerful tools for managing data transfers between your storage systems. This extension to the main Apolo CLI enables seamless movement of data between external storage systems and your Apolo cluster, as well as transfers between different clusters.

For complete details on Apolo Extras CLI refer to the [CLI reference](https://app.gitbook.com/s/EicNFI9vPOX1TTMYRKT9/cli).

**Copying Data with apolo-extras data cp**

The `apolo-extras data cp` command serves as a bridge between external storage systems and your Apolo cluster. It supports multiple major cloud storage providers and protocols:

* Amazon Web Services (AWS) S3
* Google Cloud Storage (GCS)
* Microsoft Azure Blob Storage
* HTTP/HTTPS endpoints

Let's explore how to use this command effectively:

**Basic Data Copy Operations**

To copy data between storage systems, use this basic syntax:

```bash
apolo-extras data cp SOURCE DESTINATION
```

For example, to download data from S3 to your cluster storage:

```bash
apolo-extras data cp s3://my-bucket/dataset.zip storage:/data/
```

Or to upload data to Google Cloud Storage:

```bash
apolo-extras data cp storage:/results/experiment1 gs://my-bucket/results/
```

**Working with Archives**

The tool provides built-in compression and extraction capabilities. This is particularly useful when dealing with large datasets:

For extraction:

```bash
# Extract a downloaded archive directly into storage
apolo-extras data cp -x s3://datasets/images.tar.gz storage:/data/images/
```

For compression:

```bash
# Compress data before uploading
apolo-extras data cp -c storage:/results/experiment1 s3://results/exp1.tar.gz
```

The system automatically supports various archive formats:

* .tar.gz, .tgz (Gzipped tar archives)
* .tar.bz2, .tbz (Bzip2 compressed tar archives)
* .tar (Uncompressed tar archives)
* .gz (Gzip compressed files)
* .zip (ZIP archives)

**Resource Management**

You can control the resources allocated for data transfer operations:

```bash
# Use a specific compute preset
apolo-extras data cp -s gpu-small s3://large-dataset.zip storage:/data/

# Set a custom lifespan for long transfers
apolo-extras data cp -l 7200 storage:/huge-dataset gs://backup/
```

**Transferring Between Clusters**

The `apolo-extras data transfer` command is specifically designed for moving data between different Apolo clusters. This is particularly useful for:

* Migrating datasets between regions
* Sharing data between development and production environments
* Creating backups across clusters

Basic usage:

```bash
apolo-extras data transfer storage:/sourcedata storage://{other-cluster}/destination/
```



---
File: /docs/apolo-concepts-cli/apps/images.md
---

# Images

## Overview

The Images app provides a central location for viewing properties of container image assets used in deployments. For more information about the images App and how to use it in Apolo Console, visit the main [Images app](../../apolo-console/apps/pre-installed/images.md) page.

## **Command Line Interface**

While the Images app provides a graphical interface for viewing image properties, the Apolo CLI offers powerful commands for managing container images directly from your terminal. The `apolo image` command suite includes the following operations:

### **Basic Commands**

* `apolo image ls`: Lists images in your current project and cluster. Supports filtering by name, organization, and project.
* `apolo image tags`: Lists all tags associated with an image.
* `apolo image rm`: Removes images from the platform registry.
* `apolo image size`: Shows the size of a specific image.
* `apolo image digest`: Retrieves the digest of an image from the remote registry.

### **Working with Images**

The most commonly used operations are pushing and pulling images. Here's how to use them effectively:

Pushing images to the registry:

```bash
# Push a local image using the 'latest' tag
apolo image push myimage

# Push with a specific tag and destination
apolo image push alpine:latest image:my-alpine:production

# Push to a different project
apolo image push alpine image:/other-project/alpine:shared
```

Pulling images from the registry:

```bash
# Pull an image to your local environment
apolo image pull image:myimage

# Pull with a different local name
apolo image pull image:/project/my-alpine:production alpine:from-registry

# Pull from another project
apolo image pull image:/other-project/alpine:shared
```

### **Image Naming Convention**

When working with the CLI, image names follow a specific URL scheme:

* Remote images must use the `image://` scheme
* Tags can be specified using the colon notation (e.g., `image:myapp:v1.0`)
* Cross-project references use the format `image:/other-project/imagename:tag`

Note: All commands provide additional help information through the `--help` option, which details available flags and usage examples.

### **Using External Images**

While the Images app and CLI provide tools for managing images in the platform registry, you can also run jobs using external Docker images. Simply specify the full image path when using `apolo job run`:

```bash
# Run a job using an image from Docker Hub
apolo job run pytorch/pytorch:latest

# Run a job with a custom entrypoint using an external image
apolo job run --preset=gpu-small --entrypoint=/custom-script.sh tensorflow/tensorflow:latest -- arg1 arg2
```

This flexibility allows you to leverage both platform-hosted images and publicly available container images from Docker Hub or other registries, depending on your needs. The same job configuration options apply regardless of whether you're using internal or external images.

### **Working with Images in Workflows**

Apolo Workflows provide a powerful way to automate image building and management as part of your development process. While you can build images directly using the CLI, workflows offer more sophisticated features for image handling, especially when working with complex build requirements or multiple image variants.

#### **Defining Images in Live Workflows**

In your `.apolo/live.yml` file, you can define images under the `images` section. Each image definition can specify its build context, Dockerfile location, build arguments, and resulting reference. Here's an example:

```yaml
images:
  training_image:
    context: ./training
    dockerfile: Dockerfile.training
    ref: image:training:${{ hash_files('training/Dockerfile.training', 'training/requirements.txt') }}
    build_args:
      - PYTHON_VERSION=3.9
    
  inference_image:
    context: ./inference
    ref: image:inference:latest
    build_preset: gpu-small
    env:
      CUDA_VERSION: "11.8"
```

This workflow defines two images with different configurations. The `training_image` uses content-based tagging through the `hash_files` function, which automatically generates a new tag when the source files change. The `inference_image` uses a GPU-enabled preset for its build process.

#### **Using Workflow Images in Jobs**

Once defined, these images can be referenced in your workflow jobs:

```yaml
jobs:
  train_model:
    image: ${{ images.training_image.ref }}
    preset: gpu-large
    volumes:
      - storage:data:/data
    cmd: python train.py --data-path /data

  serve_model:
    image: ${{ images.inference_image.ref }}
    http_port: 8080
    env:
      MODEL_PATH: /models/latest
```

#### **Building Images with Workflows**

To build images defined in your workflow, use the `apolo-flow build` command:

```bash
# Build a specific image
apolo-flow build training_image

# Force rebuild even if the image exists
apolo-flow build -F inference_image
```

The workflow system handles the entire build process, including:

* Setting up the build environment according to your specifications
* Managing build arguments and environment variables
* Uploading the build context to the platform
* Building the image using Kaniko in the cloud
* Publishing the resulting image to the platform registry

#### **Advanced Build Features**

Workflows provide several advanced features for image building:

* Content-based tagging using `hash_files()` for automatic version management
* Build-time secret management through environment variables and mounted volumes
* Resource preset selection for builds requiring specific hardware
* Build argument and environment variable interpolation using workflow expressions

This integration of image building into workflows allows you to create reproducible, automated processes for managing your container images as part of your larger application lifecycle.

For detailed information about workflow syntax and capabilities, refer to our [workflow documentation](https://docs.apolo.us/index/apolo-flow-reference). All image-related operations in workflows follow the same naming conventions described in the CLI section above.

### **Building Custom Images without Workflows**

The Apolo Extras CLI provides powerful tools for building and managing custom container images. This functionality is available through the `apolo-extras image` command suite, which offers two main approaches to building images:

Remote Building:

```bash
# Build an image remotely using Kaniko
apolo-extras image build ./app-context image:myapp:v1.0

# Build with custom Dockerfile and build arguments
apolo-extras image build -f custom.Dockerfile --build-arg VERSION=1.0 ./app-context image:myapp:latest
```

Local Building:

```bash
# Build an image locally using your Docker daemon
apolo-extras image local-build ./app-context image:myapp:v1.0
```

The remote build option uses Kaniko to construct images directly on the cluster, which is particularly useful when you don't have Docker installed locally or need to access cluster-specific resources during the build process. The local build option leverages your local Docker daemon, providing a familiar development experience.

Additionally, you can transfer images between clusters using:

```bash
apolo-extras image transfer image:myapp:v1.0 image:/other-cluster/myapp:v1.0
```

For detailed information about image building options, including advanced Kaniko configurations and build customization, please refer to the [Apolo Extras CLI](https://app.gitbook.com/s/EicNFI9vPOX1TTMYRKT9/) documentation.



---
File: /docs/apolo-concepts-cli/apps/jobs.md
---

---
description: Running jobs using the Apolo CLI
---

# Jobs

## Overview

The **Jobs** App is a tool that allows users to schedule and execute containerized tasks and processes. It provides a user-friendly interface to manage these workloads, simplifying tasks like data processing, model training and inference, and other batch jobs. This app is designed to provide flexibility and control over how these jobs are run, while offering monitoring features for insights and debugging. For more information about the Jobs app, as well as detailed instruction of how to use it in Apolo Console, visit the main [Jobs app](../../apolo-console/apps/pre-installed/jobs/) page.

### **Running Jobs Using the CLI**

The `apolo job run` command lets you execute containerized workloads with precise control over their configuration. Let's explore how to create and configure jobs effectively using the CLI (see [Apolo CLI reference](https://docs.apolo.us/index/apolo-cli/commands/job#run) for more information on running jobs).

**Basic Job Execution** At its most basic, you only need to specify a Docker image to run a job:

```bash
apolo job run pytorch/pytorch:latest
```

This command runs the image with default settings. However, you'll often want to customize how your job runs.

**Essential Job Configuration**

Let's look at the core parameters you can configure when running a job:

**Container Configuration**

```bash
# Specify the command to run in the container
apolo job run pytorch/pytorch:latest -- python train.py --epochs 100

# Set a custom entrypoint
apolo job run --entrypoint=/custom_script.sh pytorch/pytorch:latest

# Set the working directory inside the container
apolo job run --workdir /workspace pytorch/pytorch:latest
```

**Environment and Data** You can pass data and configuration to your jobs in several ways:

```bash
# Set individual environment variables
apolo job run --env BATCH_SIZE=32 --env LEARNING_RATE=0.001 pytorch/pytorch:latest

# Load environment variables from a file
apolo job run --env-file config.env pytorch/pytorch:latest

# Mount storage volumes
apolo job run --volume storage::/data:rw --volume storage:/public:/public:ro pytorch/pytorch:latest
```

The volume syntax follows the pattern `storage:source:destination:mode`, where mode can be `rw` (read-write) or `ro` (read-only).

**Resource Allocation** Control the computing resources available to your job:

```bash
# Select a predefined resource configuration
apolo job run --preset gpu-small pytorch/pytorch:latest

# Request extended shared memory
apolo job run --extshm pytorch/pytorch:latest
```

**Job Identity and Organization** Give your job meaningful identifiers for better management:

```bash
# Assign a name to your job
apolo job run --name training-experiment-v1 pytorch/pytorch:latest

# Add a description
apolo job run --description "Training run with modified hyperparameters" pytorch/pytorch:latest

# Add tags for organization
apolo job run --tag experiment --tag v1 pytorch/pytorch:latest
```

**Runtime Behavior** Configure how your job behaves during execution:

```bash
# Set a maximum runtime for the job
apolo job run --life-span 12h pytorch/pytorch:latest

# Configure automatic restart behavior
apolo job run --restart on-failure pytorch/pytorch:latest

# Set job priority
apolo job run --priority high pytorch/pytorch:latest
```

**Network and HTTP Configuration** If your job serves HTTP content or needs port forwarding:

```bash
# Enable HTTP port forwarding (default port 80)
apolo job run --http-port 8080 pytorch/pytorch:latest

# Forward specific ports to your local machine
apolo job run --port-forward 8888:8888 pytorch/pytorch:latest

# Control HTTP authentication
apolo job run --no-http-auth pytorch/pytorch:latest
```

**Interactive Jobs** For jobs requiring interaction:

```bash
# Allocate a TTY for interactive use
apolo job run --tty pytorch/pytorch:latest

# Run without attaching to the job
apolo job run --detach pytorch/pytorch:latest
```

**Project and Organization Context** Specify where your job should run:

```bash
# Run in a specific project
apolo job run --project ml-experiments pytorch/pytorch:latest

# Run in a specific organization
apolo job run --org research-team pytorch/pytorch:latest

# Run on a specific cluster
apolo job run --cluster gpu-cluster pytorch/pytorch:latest
```

You can combine these options to create precisely configured jobs. Here's an example that brings together several common options:

```bash
apolo job run \
    --name training-run \
    --preset gpu-small \
    --volume storage::/data:rw \
    --env BATCH_SIZE=32 \
    --env LEARNING_RATE=0.001 \
    --workdir /workspace \
    --life-span 24h \
    --tag experiment \
    --description "Training run with custom parameters" \
    pytorch/pytorch:latest \
    -- python train.py --epochs 100
```

This comprehensive command creates a named job with custom resource allocation, mounted storage, environment variables, a working directory, runtime limit, and organizational tags, then executes a specific Python script with custom parameters.

Remember that after starting a job, you can monitor its progress using commands like `apolo job logs` to view output and `apolo job status` to check its current state.

I'll create a comprehensive section about debugging jobs that builds on the previous content and provides clear, practical explanations.

## **Debugging Jobs**

When developing and running containerized workloads, you'll often need to troubleshoot issues, monitor performance, or inspect the internal state of your jobs. Apolo provides several powerful tools to help you debug and understand your running jobs effectively.

### **Investigating Job Status and Logs**

The first step in debugging is understanding what's happening with your job. Apolo provides several ways to inspect your job's status and output:

```bash
# View detailed status of a specific job
apolo job status my-training-job

# Stream real-time logs from your job
apolo job logs my-training-job

# See logs with timestamps for correlation
apolo job logs --timestamps my-training-job

# View logs from a specific time period
apolo job logs --since 1h my-training-job
```

When you have many jobs running, you can filter the job list to find the ones you're interested in:

```bash
# Find jobs by status
apolo job ls --status failed --status running

# Search by name
apolo job ls --name training-experiment

# Filter by creation time
apolo job ls --since 2h --recent-first
```

### **Interactive Debugging**

Sometimes you need to interact directly with a running job. Apolo provides two powerful commands for this purpose:

```bash
# Start a new shell in the running container
apolo job exec my-training-job -- /bin/bash

# Execute a specific command
apolo job exec my-training-job -- ps aux
```

### **Port Forwarding for Web-Based Debugging**

Many debugging tools provide web interfaces. You can access these using Apolo's port forwarding capabilities:

```bash
# Forward multiple ports for different debugging tools
apolo job port-forward my-training-job \
    8080:8080 \  # For your application
    6006:6006 \  # For TensorBoard
    8888:8888    # For Jupyter notebooks

# Forward ports with HTTP authentication
apolo job run --http-port 8080 --http-auth my-image:latest
```

### **Attaching to Running Jobs**

The `apolo job attach` command creates an interactive connection to a running job, allowing you to observe its output and interact with it in real-time. This is particularly useful when you need to monitor progress, investigate issues, or work with interactive applications.

Basic attachment is straightforward:

```bash
apolo job attach my-training-job
```

This connects your terminal's input and output streams to the running job, letting you see any output and interact with the job directly. You can detach from the session without stopping the job by pressing Ctrl+P followed by Ctrl+Q.

A powerful feature of attach is its ability to combine terminal access with port forwarding. This is especially valuable when debugging applications that expose network services, like web servers or Jupyter notebooks:

```bash
# Attach and forward ports for both console access and web interfaces
apolo job attach my-debug-job \
    --port-forward 8888:8888 \  # For Jupyter
    --port-forward 6006:6006    # For TensorBoard
```

This command gives you both console access to your job and the ability to reach any network services through your local ports. For instance, with the above command, you could monitor training output in the console while accessing Jupyter at localhost:8888 and TensorBoard at localhost:6006 in your browser.

When debugging with attach, you can run additional Apolo commands in separate terminals to get a complete picture of your job's behavior. For example, you might run `apolo job top` in another terminal to monitor resource usage while interacting with your attached session.

Remember that closing your attach session doesn't terminate the job – it continues running in the background. You can always reattach to check on its progress or continue debugging as needed.

### **Preserving Job State**

After debugging and fixing issues, you might want to save the state of your container for future use or analysis. The `apolo job save` command creates a new image from your job's current state:

```bash
# Save the current state as a new image
apolo job save my-training-job image:debug-checkpoint-v1

# You can then use this image to start a new job
apolo job run image:debug-checkpoint-v1
```

This is particularly useful when:

* You've made changes to the container during debugging
* You want to capture the exact state where an issue occurred
* You need to share a reproducible environment with colleagues

### Monitoring resource usage

Use the following commands to display GPU, CPU and memory usage in a job.

```bash
# Watch resource utilization in real-time
apolo job top my-training-job

# Sort jobs by CPU or memory usage
apolo job top --sort cpu
```



---
File: /docs/apolo-concepts-cli/apps/README.md
---

# Apps

The Apolo console offers two categories of applications: Pre-installed Apps and [Available Apps](../../documentation/english/core/apps/available-apps/). This section will go over how you can use Apolo CLI to interact with Apps in Apolo.

#### Pre-installed Apps

Pre-installed apps are essential tools that come standard with the Apolo console, giving ML engineers instant access to key functionalities and facilitating efficient processes without requiring any additional setup. These apps a core part of the platform core and can be interacted with using Apolo CLI.

#### Available Apps

Available apps are a collection of popular and widely-used tools in the machine learning industry. These apps are not installed by default and must be installed before you can use them. You can explore and install any of these apps according to your project requirements. These apps are installable experiences and can currently only be managed using Apolo Console.




---
File: /docs/apolo-concepts-cli/installing.md
---

# Installing CLI

[Apolo Web Shell](https://console.apolo.us/apps/shell/install) application doesn't require installation and can quickly get you familiar with Apolo, allowing you to work with the platform in a browser.

Installing Apolo CLI locally can be more efficient for long-term use, as your source code and other local files will be stored directly on your machine. Additionally, using Apolo CLI provides you with more flexible and extensive functionality, allowing for greater control and customization of your development environment.

## Installation instructions

{% tabs %}
{% tab title="Linux and Mac OS" %}
**Installing via pipx**

Our _apolo-all_ package available in pipx will automatically install all required components:

```
pip install pipx
pipx install apolo-all
pipx upgrade apolo-all
```

**Installing via pip**

You can also install all of the components through pip.

Apolo CLI requires Python 3 installed (recommended: 3.8; required: 3.7.9 or newer). We suggest using the [Anaconda Python 3.8 Distribution](https://www.anaconda.com/distribution/).

```
pip install -U apolo-cli apolo-extras apolo-flow
apolo login
```

If your machine doesn't have GUI, use the following command instead of apolo login:

```
apolo config login-headless
```
{% endtab %}

{% tab title="Windows" %}
**Installing via pipx**

Our _apolo-all_ package available in pipx will automatically install all required components:

```
pip install pipx
pipx install apolo-all
pipx upgrade apolo-all
```

**Installing via pip**

You can also install all of the components through pip.

We highly recommend using the [Anaconda Python 3.8 Distribution](https://www.anaconda.com/distribution/) with default installation settings.

When you have it up and running, run the following commands in Conda Prompt:

```
conda install -c conda-forge make
conda install -c conda-forge git    
pip install -U apolo-cli apolo-extras apolo-flow
pip install -U certifi
apolo login
```

To make sure that all commands you can find in our documentation work properly, don't forget to run `bash` every time you open Conda Prompt.
{% endtab %}
{% endtabs %}



---
File: /docs/apolo-console/apps/available-apps/llm-inference/multi-gpu-benchmarks-report.md
---

---
description: >-
  This is a report summarizing the benchmark methodology, the environment, the
  metrics, and the conclusions based on the data we collected.
---

# Multi-GPU Benchmarks Report

1\. Introduction

We conducted a series of **vLLM** inference benchmarks to evaluate performance under different **GPU presets**, **model sizes**, and **parallelization strategies** (pipeline vs. tensor). We focused on:

* **Prompt tokens/s** and **generation tokens/s** (throughput).
* **Requests** in different states (running, swapped, waiting).
* **KV-cache usage** on **GPU** and **CPU**.
* **Average request latencies**.
* **Error counts** (e.g., OOM or network-related failures).

These tests spanned a range of **context lengths** (from **2048** up to **128k** tokens) and **model sizes** (e.g., 1.5B, 8B, 32B). We also **compared pipeline parallel** with **tensor parallel** deployments to see how different parallelization strategies impacted throughput.

### 2. Environment & Setup

#### 2.1 GPU Presets

We used the following GPU presets, each with distinct CPU, memory, and GPU counts/types:

| **Preset** | **vCPUs** | **Memory** | **VRAM** | **GPU Count** | **GPU Type**            |
| ---------- | --------- | ---------- | -------- | ------------- | ----------------------- |
| gpu-small  | 30.0      | 63.0 GB    | 16 GB    | 1             | NVIDIA V100 (PCIe 16GB) |
| gpu-medium | 60.0      | 126.0 GB   | 32 GB    | 2             | NVIDIA V100 (PCIe 16GB) |
| gpu-large  | 120.0     | 252.0 GB   | 64 GB    | 4             | NVIDIA V100 (PCIe 16GB) |
| gpu-xlarge | 120.0     | 504.0 GB   | 128 GB   | 8             | NVIDIA V100 (PCIe 16GB) |
| mi210x1    | 15        | 65.0 GB    | 64 GB    | 1             | AMD MI210               |
| mi210x2    | 30        | 130.0 GB   | 128 GB   | 2             | AMD MI210               |
| H100X1     | 63.0      | 265.0 GB   | 80 GB    | 1             | NVIDIA H100 (PCIe 80GB) |
| H100X2     | 126.0     | 530.0 GB   | 160 GB   | 2             | NVIDIA H100 (PCIe 80GB) |

Each preset was deployed via a Helm-based “apolo” flow.

#### 2.2 Models

We tested multiple Hugging Face models:

* **`deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`**` ``(smaller ~1.5B params)`
* **`meta-llama/Llama-3.2-3B-Instruct`**` ``(~3B params)`
* **`meta-llama/Llama-3.1-8B-Instruct`**` ``(~8B params)`
* **`deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`**` ``(~32B params)`

We then varied **context length** from 2048 up to 128k tokens to measure how throughput, memory usage, and latencies scaled with input size.

#### 2.3 Benchmark Script & Methodology

A custom Python script:

1. **Deploys** each (preset, model) combination,\
   With the following arguments:\
   `--host=0.0.0.0 --port=8000 --model=meta-llama/Llama-3.1-8B-Instruct --code-revision=main --tokenizer= --tensor-parallel-size=<number_of_gpus> --dtype=half --max-model-len=<context_length> --enforce-eager --trust-remote-code`\
   For context length we use a different length for each run and for tensor-parallel-size we use the number of GPUs available on the preset
2. **Waits** until the endpoint is ready (`/v1/models` returning 200),
3. **Sends** load (e.g., 100 requests) at concurrency=1,&#x20;
   * 100 requests @10req at a time to the `/v1/completions` endpoint
   * Uses a fixed prompt: "Let's explore some architecture patterns for microservices"
   * Configures max\_tokens=512/2048 and temperature=0.7&#x20;
4. **Polls** `/metrics` every second for:
   * `prompt_tokens_total` & `generation_tokens_total` => used to compute tokens/s
   * `num_requests_running`, `num_requests_swapped`, `num_requests_waiting`
   * `gpu_cache_usage_perc`, `cpu_cache_usage_perc`
5. **Tracks** per-request latencies and errors,
6. **Continues** polling until all requests are finalized (no pending/running/swapped),
7. **Writes** aggregated metrics (averages) into a CSV file,
8. **Generates** bar charts for each metric.

We repeated these steps for **pipeline parallel** vs. **tensor parallel** where relevant.

### 3. Overview of Parallel Strategies

1. **Pipeline Parallel**: Splits the model layers into stages across multiple GPUs so that each GPU processes a portion of layers in sequence.
2. **Tensor Parallel**: Splits _tensors_ (e.g., weight matrices) across multiple GPUs in a more fine-grained way so the same layers are effectively distributed among GPUs.

**In general**, **tensor parallel** is often more efficient for large or similarly sized GPUs, whereas **pipeline parallel** can help in some multi-GPU cases but can introduce significant inter-stage waiting time and memory overheads, especially if each pipeline stage has different computational loads.

Below are **side-by-side tables** comparing **pipeline parallel** vs. **tensor parallel** for  **Llama-3B at 2048 context length** —where we have overlapping data. Each cell shows **(Prompt TPS, Generation TPS)**. After each table, we list **observations** for that model.

#### **Llama-3.2-3B-Instruct -  2048 context length @10req concurrency for 100 total requests**&#x20;

<table><thead><tr><th width="142">GPU Preset</th><th width="184">Pipeline (Prompt TPS)</th><th width="172">Tensor (Prompt TPS)</th><th width="154">Pipeline (Gen TPS)</th><th width="146">Tensor (Gen TPS)</th><th width="168">Prompt Speedup (%)</th><th width="147">Gen Speedup (%)</th></tr></thead><tbody><tr><td>H100X1</td><td>47.64</td><td>47.35</td><td>564.79</td><td>573.80</td><td>-0.6%</td><td>1.6%</td></tr><tr><td>H100X2</td><td>36.14</td><td>40.98</td><td>449.28</td><td>500.43</td><td>13.4%</td><td>11.4%</td></tr><tr><td>gpu-medium</td><td>34.17</td><td>43.03</td><td>416.18</td><td>521.92</td><td>25.9%</td><td>25.4%</td></tr><tr><td>gpu-small</td><td>47.22</td><td>47.80</td><td>581.37</td><td>576.27</td><td>1.2%</td><td>-0.9%</td></tr><tr><td>mi210x1</td><td>47.79</td><td>46.29</td><td>581.30</td><td>574.77</td><td>-3.1%</td><td>-1.1%</td></tr><tr><td>mi210x2</td><td>34.20</td><td>40.59</td><td>425.94</td><td>489.30</td><td>18.7%</td><td>14.9%</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/llama_3B_prompt_throughput_comparison.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/llama_3B_gen_throughput_comparison.png" alt=""><figcaption></figcaption></figure>



**Observations (Llama-3B, 2048 ctx, Pipeline vs. Tensor)**

* **H100X1**: \~-0.6% prompt speedup, \~1.6% gen speedup.
* **H100X2**: \~13.4% prompt speedup, \~11.4% gen speedup.
* **gpu-medium**: \~25.9% prompt speedup, \~25.4% gen speedup.
* **gpu-small**: \~1.2% prompt speedup, \~-0.9% gen speedup.
* **mi210x1**: \~-3.1% prompt speedup, \~-1.1% gen speedup.
* **mi210x2**: \~18.7% prompt speedup, \~14.9% gen speedup.

Overall, we notice that:

* For small models, if they fit on a single GPU, splitting them across multiple GPUs doesn't help. It actually slows down inference.
* The tensor parallel size split is faster than the pipeline parallel size split on multi-gpu setups, which is expected.

### 4. Results & Observations

Below we break down **context length** runs and highlight models performance on specific configurations&#x20;

#### 4.1 2048-Token Context Benchmarks

Below we have three models: **Qwen-1.5B**, **Llama-3B**, **Llama-8B**, and **Qwen-32B**.

**4.1.1 Qwen-1.5B - 2048 context length  @10req at a time for 100 total requests**&#x20;

<table data-full-width="true"><thead><tr><th width="118">Preset</th><th width="130">Prompt TPS</th><th width="115">Gen TPS</th><th width="134">Avg Latency (s)</th><th width="224">Request Generation Level TPS</th><th width="208">Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>45.74</td><td>649.78</td><td>6.95</td><td>71.64</td><td>5.10</td><td>0</td></tr><tr><td>H100X2</td><td>37.44</td><td>521.10</td><td>8.47</td><td>57.64</td><td>4.33</td><td>0</td></tr><tr><td>gpu-large</td><td>38.09</td><td>535.91</td><td>8.35</td><td>58.93</td><td>4.43</td><td>0</td></tr><tr><td>gpu-medium</td><td>39.73</td><td>552.69</td><td>7.96</td><td>61.43</td><td>4.68</td><td>0</td></tr><tr><td>gpu-small</td><td>46.63</td><td>676.10</td><td>6.79</td><td>74.31</td><td>5.21</td><td>0</td></tr><tr><td>mi210x1</td><td>43.73</td><td>618.48</td><td>7.24</td><td>68.46</td><td>5.06</td><td>0</td></tr><tr><td>mi210x2</td><td>9.35</td><td>125.16</td><td>8.84</td><td>55.09</td><td>4.13</td><td>10</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-1.5B_2048ctx_512max.png" alt=""><figcaption></figcaption></figure>

**Observations (Qwen-1.5B, 2048 ctx)**:

* Highest **Prompt TPS**: `gpu-small` with 46.63 tokens/s
* Highest **Gen TPS**: `gpu-small` with 676.10 tokens/s
* Notable errors on: mi210x2 (10 errs)

**4.1.2 Llama-3B - 2048 context length  @10req at a time for 100 total requests**&#x20;

<table data-full-width="true"><thead><tr><th width="132">Preset</th><th>Prompt TPS</th><th width="117">Gen TPS</th><th width="141">Avg Latency (s)</th><th width="234">Request Generation Level TPS</th><th width="227">Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>9.12</td><td>105.12</td><td>7.95</td><td>64.26</td><td>5.36</td><td>10</td></tr><tr><td>H100X2</td><td>40.23</td><td>500.80</td><td>7.83</td><td>55.76</td><td>4.55</td><td>0</td></tr><tr><td>gpu-large</td><td>41.73</td><td>510.79</td><td>7.37</td><td>58.00</td><td>4.84</td><td>0</td></tr><tr><td>gpu-medium</td><td>43.03</td><td>532.96</td><td>7.24</td><td>59.75</td><td>4.91</td><td>0</td></tr><tr><td>gpu-small</td><td>47.22</td><td>576.56</td><td>6.49</td><td>65.87</td><td>5.51</td><td>0</td></tr><tr><td>gpu-xlarge</td><td>42.42</td><td>510.52</td><td>7.31</td><td>57.83</td><td>4.91</td><td>0</td></tr><tr><td>mi210x1</td><td>45.35</td><td>570.08</td><td>6.73</td><td>65.08</td><td>5.31</td><td>0</td></tr><tr><td>mi210x2</td><td>38.17</td><td>475.52</td><td>8.30</td><td>52.58</td><td>4.30</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.2-3B-Instruct_2048ctx_512max.png" alt=""><figcaption></figcaption></figure>

**Observations (Llama-3B, 2048 ctx)**

* Highest **Prompt TPS**: `gpu-small` with 47.22 tokens/s
* Highest **Gen TPS**: `gpu-small` with 576.56 tokens/s
* Notable errors on: H100X1 (10 errs)

**4.1.3 Llama-8B - 2048 context length  @10req at a time for 100 total requests**&#x20;

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>28.07</td><td>399.07</td><td>11.60</td><td>42.91</td><td>3.04</td><td>0</td></tr><tr><td>H100X2</td><td>5.08</td><td>66.26</td><td>11.01</td><td>45.72</td><td>3.19</td><td>20</td></tr><tr><td>gpu-large</td><td>34.24</td><td>492.47</td><td>9.52</td><td>52.81</td><td>3.69</td><td>0</td></tr><tr><td>gpu-medium</td><td>34.56</td><td>491.24</td><td>9.17</td><td>54.03</td><td>3.84</td><td>1</td></tr><tr><td>gpu-xlarge</td><td>34.27</td><td>488.51</td><td>9.41</td><td>52.93</td><td>3.75</td><td>0</td></tr><tr><td>mi210x1</td><td>28.09</td><td>407.72</td><td>11.66</td><td>43.22</td><td>3.02</td><td>0</td></tr><tr><td>mi210x2</td><td>31.46</td><td>444.93</td><td>10.17</td><td>48.53</td><td>3.47</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.1-8B-Instruct_2048ctx_512max.png" alt=""><figcaption></figcaption></figure>

**Observations (Llama-8B, 2048 ctx)**:

* Highest **Prompt TPS**: `gpu-medium` with 34.56 tokens/s
* Highest **Gen TPS**: `gpu-large` with 492.47 tokens/s
* Notable errors on: gpu-medium (1 errs), H100X2 (20 errs)



**4.1.4 Qwen-32B - 2048 context length  @10req at a time for 100 total requests**&#x20;

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>14.44</td><td>123.72</td><td>22.27</td><td>13.42</td><td>1.95</td><td>0</td></tr><tr><td>H100X2</td><td>20.39</td><td>175.25</td><td>15.88</td><td>18.87</td><td>2.70</td><td>0</td></tr><tr><td>gpu-xlarge</td><td>8.20</td><td>73.99</td><td>12.06</td><td>27.64</td><td>3.53</td><td>10</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-32B_2048ctx_512max.png" alt=""><figcaption></figcaption></figure>

**Observations (Qwen-32B, 2048 ctx)**:

* Highest **Prompt TPS**: `H100X2` with 20.39 tokens/s
* Highest **Gen TPS**: `H100X2` with 175.25 tokens/s
* Notable errors on: gpu-xlarge (10 errs)

#### 4.2 8192-Token Context Benchmarks

#### 4.2.1 DeepSeek-R1-Distill-Qwen-1.5B **- 8192 context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>23.80</td><td>605.55</td><td>12.79</td><td>69.47</td><td>3.21</td><td>0</td></tr><tr><td>H100X2</td><td>20.07</td><td>517.68</td><td>15.33</td><td>58.55</td><td>2.89</td><td>0</td></tr><tr><td>gpu-large</td><td>20.76</td><td>531.39</td><td>15.24</td><td>58.74</td><td>2.61</td><td>0</td></tr><tr><td>gpu-medium</td><td>22.98</td><td>551.03</td><td>13.77</td><td>61.23</td><td>2.97</td><td>0</td></tr><tr><td>gpu-small</td><td>27.97</td><td>666.18</td><td>11.56</td><td>71.97</td><td>3.87</td><td>0</td></tr><tr><td>mi210x1</td><td>24.30</td><td>602.95</td><td>12.67</td><td>68.55</td><td>3.41</td><td>0</td></tr><tr><td>mi210x2</td><td>19.05</td><td>469.01</td><td>17.02</td><td>50.65</td><td>2.56</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-1.5B_8192ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `gpu-small` with 27.97 tokens/s
* Highest **Gen TPS**: `gpu-small` with 666.18 tokens/s

#### 4.2.2 Llama-3.2-3B-Instruct **- 8192 context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>37.67</td><td>522.51</td><td>8.28</td><td>58.67</td><td>4.70</td><td>0</td></tr><tr><td>H100X2</td><td>38.42</td><td>496.42</td><td>8.23</td><td>55.05</td><td>4.63</td><td>0</td></tr><tr><td>gpu-large</td><td>40.86</td><td>523.26</td><td>7.82</td><td>57.39</td><td>4.85</td><td>0</td></tr><tr><td>gpu-medium</td><td>38.88</td><td>531.07</td><td>8.23</td><td>58.16</td><td>4.70</td><td>0</td></tr><tr><td>gpu-small</td><td>38.51</td><td>521.73</td><td>7.22</td><td>65.37</td><td>5.23</td><td>0</td></tr><tr><td>gpu-xlarge</td><td>36.69</td><td>512.53</td><td>8.55</td><td>56.85</td><td>4.64</td><td>0</td></tr><tr><td>mi210x1</td><td>37.78</td><td>545.31</td><td>7.66</td><td>64.91</td><td>5.36</td><td>1</td></tr><tr><td>mi210x2</td><td>29.98</td><td>421.53</td><td>9.11</td><td>53.83</td><td>4.29</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.2-3B-Instruct_8192ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `gpu-large` with 40.86 tokens/s
* Highest **Gen TPS**: `mi210x1` with 545.31 tokens/s
* Notable errors on: mi210x1 (1 errs)

#### 4.2.3 Llama-8B **- 8192 context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>8.27</td><td>369.33</td><td>23.56</td><td>39.56</td><td>2.18</td><td>63</td></tr><tr><td>H100X2</td><td>7.83</td><td>382.46</td><td>26.82</td><td>41.91</td><td>2.05</td><td>64</td></tr><tr><td>gpu-large</td><td>10.82</td><td>493.55</td><td>30.12</td><td>52.87</td><td>1.78</td><td>0</td></tr><tr><td>gpu-medium</td><td>10.18</td><td>503.87</td><td>32.15</td><td>53.54</td><td>1.53</td><td>0</td></tr><tr><td>gpu-xlarge</td><td>10.79</td><td>494.30</td><td>30.44</td><td>52.60</td><td>1.74</td><td>0</td></tr><tr><td>mi210x1</td><td>8.10</td><td>397.21</td><td>40.79</td><td>41.65</td><td>1.25</td><td>0</td></tr><tr><td>mi210x2</td><td>10.57</td><td>455.34</td><td>30.63</td><td>48.88</td><td>1.81</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.1-8B-Instruct_8192ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations (Llama-8B, 8192 ctx)**

* Highest **Prompt TPS**: `gpu-large` with 10.82 tokens/s
* Highest **Gen TPS**: `gpu-medium` with 503.87 tokens/s
* Notable errors on: H100X1 (63 errs), H100X2 (64 errs)

#### 4.2.4 Qwen-32B  **- 8192 context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>11.49</td><td>116.34</td><td>22.60</td><td>13.39</td><td>1.91</td><td>14</td></tr><tr><td>H100X2</td><td>17.82</td><td>160.93</td><td>16.17</td><td>18.63</td><td>2.89</td><td>2</td></tr><tr><td>gpu-xlarge</td><td>25.81</td><td>229.41</td><td>11.28</td><td>27.48</td><td>3.97</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-32B_8192ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `gpu-xlarge` with 25.81 tokens/s
* Highest **Gen TPS**: `gpu-xlarge` with 229.41 tokens/s
* Notable errors on: H100X1 (14 errs), H100X2 (2 errs)

#### 4.3 64k-Token Context Benchmarks

#### 4.3.1 Qwen-1.5B **-** 64k **context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>24.50</td><td>621.06</td><td>13.04</td><td>68.12</td><td>3.35</td><td>0</td></tr><tr><td>H100X2</td><td>7.58</td><td>181.16</td><td>14.96</td><td>57.85</td><td>2.85</td><td>10</td></tr><tr><td>mi210x1</td><td>24.49</td><td>609.78</td><td>12.68</td><td>68.15</td><td>3.29</td><td>0</td></tr><tr><td>mi210x2</td><td>18.45</td><td>502.88</td><td>17.12</td><td>54.94</td><td>2.48</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-1.5B_64000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `H100X1` with 24.50 tokens/s
* Highest **Gen TPS**: `H100X1` with 621.06 tokens/s
* Notable errors on: H100X2 (10 errs)

#### 4.3.2 Llama-3.2-3B **-** 64k **context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>45.85</td><td>570.00</td><td>6.74</td><td>64.60</td><td>5.40</td><td>0</td></tr><tr><td>H100X2</td><td>40.34</td><td>501.89</td><td>7.80</td><td>55.93</td><td>4.71</td><td>0</td></tr><tr><td>mi210x1</td><td>40.51</td><td>595.07</td><td>7.85</td><td>65.21</td><td>5.22</td><td>0</td></tr><tr><td>mi210x2</td><td>30.43</td><td>419.55</td><td>9.04</td><td>53.19</td><td>4.30</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.2-3B-Instruct_64000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `H100X1` with 45.85 tokens/s
* Highest **Gen TPS**: `mi210x1` with 595.07 tokens/s

#### 4.3.3 Llama-3.1-8B **-** 64k **context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>8.35</td><td>367.05</td><td>19.59</td><td>39.50</td><td>2.53</td><td>65</td></tr><tr><td>H100X2</td><td>8.09</td><td>386.26</td><td>34.04</td><td>41.59</td><td>1.64</td><td>41</td></tr><tr><td>mi210x2</td><td>8.65</td><td>451.61</td><td>38.24</td><td>47.71</td><td>1.26</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.1-8B-Instruct_64000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `mi210x2` with 8.65 tokens/s
* Highest **Gen TPS**: `mi210x2` with 451.61 tokens/s
* Notable errors on: H100X1 (65 errs), H100X2 (41 errs)

#### 4.3.4 DeepSeek-R1-Distill-Qwen-32B **-** 64k **context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X2</td><td>19.32</td><td>176.10</td><td>15.99</td><td>19.06</td><td>2.91</td><td>2</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-32B_64000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `H100X2` with 19.32 tokens/s
* Highest **Gen TPS**: `H100X2` with 176.10 tokens/s
* Notable errors on: H100X2 (2 errs)

#### 4.4 128k-Token Context Benchmarks

#### 4.4.1 Qwen-1.5B **- 128k context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>26.45</td><td>642.54</td><td>11.98</td><td>70.88</td><td>3.45</td><td>0</td></tr><tr><td>H100X2</td><td>21.76</td><td>536.27</td><td>14.77</td><td>58.37</td><td>2.87</td><td>0</td></tr><tr><td>mi210x1</td><td>24.13</td><td>618.17</td><td>13.10</td><td>68.26</td><td>3.22</td><td>0</td></tr><tr><td>mi210x2</td><td>17.80</td><td>494.41</td><td>17.49</td><td>54.64</td><td>2.40</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-1.5B_128000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `H100X1` with 26.45 tokens/s
* Highest **Gen TPS**: `H100X1` with 642.54 tokens/s

#### 4.4.2 Llama-3.2-3B **- 128k context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>45.53</td><td>574.22</td><td>6.84</td><td>64.60</td><td>5.30</td><td>0</td></tr><tr><td>H100X2</td><td>30.05</td><td>451.14</td><td>9.50</td><td>55.15</td><td>4.41</td><td>0</td></tr><tr><td>mi210x1</td><td>44.17</td><td>574.07</td><td>7.08</td><td>64.16</td><td>5.30</td><td>0</td></tr><tr><td>mi210x2</td><td>32.06</td><td>444.00</td><td>9.42</td><td>51.15</td><td>4.19</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.2-3B-Instruct_128000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `H100X1` with 45.53 tokens/s
* Highest **Gen TPS**: `H100X1` with 574.22 tokens/s

#### 4.4.3 Llama-3.1-8B **- 128k context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X1</td><td>7.10</td><td>360.40</td><td>27.75</td><td>40.10</td><td>2.00</td><td>80</td></tr><tr><td>H100X2</td><td>8.38</td><td>381.71</td><td>28.39</td><td>41.35</td><td>1.95</td><td>49</td></tr><tr><td>mi210x2</td><td>10.08</td><td>467.43</td><td>32.70</td><td>49.46</td><td>1.62</td><td>0</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_meta-llama_Llama-3.1-8B-Instruct_128000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `mi210x2` with 10.08 tokens/s
* Highest **Gen TPS**: `mi210x2` with 467.43 tokens/s
* Notable errors on: H100X1 (80 errs), H100X2 (49 errs)

#### 4.4.4 DeepSeek-R1-Distill-Qwen-32B **- 128k context length  @10req at a time for 100 total requests**

<table data-full-width="true"><thead><tr><th>Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th>Avg Latency (s)</th><th>Request Generation Level TPS</th><th>Request Prompt Level TPS</th><th>Errors</th></tr></thead><tbody><tr><td>H100X2</td><td>18.96</td><td>168.05</td><td>16.02</td><td>18.98</td><td>2.90</td><td>1</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-32B_128000ctx_2048max.png" alt=""><figcaption></figcaption></figure>

**Observations**

* Highest **Prompt TPS**: `H100X2` with 18.96 tokens/s
* Highest **Gen TPS**: `H100X2` with 168.05 tokens/s
* Notable errors on: H100X2 (1 errs)



### 5. Overview of concurrency strategies

Concurrency significantly impacts overall system throughput. You will observe that the request-level tokens per second (TPS) decreases as concurrency rises, while the total system throughput increases due to the vLLMs Paged Attention algorithm and other enhancements. This aspect can be adjusted for various trade-offs to boost system throughput, accommodate a reasonable number of request level tokens per second, and reduce errors.

<table data-full-width="true"><thead><tr><th width="120">Preset</th><th>Prompt TPS</th><th>Gen TPS</th><th width="144">Avg Latency (s)</th><th width="237">Request Generation Level TPS</th><th width="210">Request Prompt Level TPS</th><th width="114" data-type="number">Concurrency</th><th>Errors</th></tr></thead><tbody><tr><td>H100X2</td><td>18.96</td><td>168.05</td><td>16.02</td><td>18.98</td><td>2.90</td><td>10</td><td>1</td></tr><tr><td>H100X2</td><td>3.62</td><td>29.36</td><td>10.2027</td><td>29.45</td><td>3.62</td><td>1</td><td>0</td></tr></tbody></table>



<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-32B_128000ctx_2048max (1).png" alt=""><figcaption><p>Concurrency of 10req at a time</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/chart_deepseek-ai_DeepSeek-R1-Distill-Qwen-32B_128000ctx_2048max (2).png" alt=""><figcaption><p>Concurrency of 1req at a time</p></figcaption></figure>

### **Important notes**

1. The script uses a short, fixed prompt, which can lead to high generation throughput.
2. It employs sequential concurrent requests, maximizing GPU utilization.
3. The powerful hardware capabilities align with these performance figures.
4. You can squeeze a lot more from these presets with multiple model instances on same GPUs.










---
File: /docs/apolo-console/apps/available-apps/llm-inference/README.md
---

# LLM Inference

[vLLM](https://github.com/vllm-project/vllm) is a high-performance and memory-efficient inference engine for large language models. It uses a novel GPU KV cache management strategy to serve transformer-based models at scale, supporting multiple GPUs (including NVIDIA and AMD) with ease. vLLM enables fast decoding and efficient memory utilization, making it suitable for production-level deployments of large LLMs.

#### Key Features

* **High Throughput Inference**: Novel GPU KV caching enables faster token generation compared to traditional implementations.
* **Multi-GPU Support**: Scales seamlessly to multiple GPUs, including AMD (MI200s, MI300s) and NVIDIA (V100/H100/A100) resource pools.
* **Easy Model Downloading**: Built-in integration with Hugging Face model repositories.
* **Flexible Configuration**: Control precision (`--dtype`), context window size, parallelism (`tensor-parallel-size`, `pipeline-parallel-size`), etc.
* **Lightweight & Extensible**: Minimal overhead for deployment and easy to integrate with existing MLOps or monitoring solutions.

#### Installation and Deployment on Apolo

You can deploy vLLM on the Apolo platform using the **`LLM Inference`** app. Apolo automates resource allocation, persistent storage, ingress, GPU detection, and environment variable injection, so you can focus on model configuration.

**Highlights of the Apolo Installation Flow**:

1. **Resource Allocation**: Choose an Apolo preset (e.g. `gpu-xlarge`, `mi210x2`) that specifies CPU, memory, and GPU resources.
2. **GPU Auto-Configuration**: If your preset includes multiple GPUs, environment variables (e.g. `CUDA_VISIBLE_DEVICES` or `HIP_VISIBLE_DEVICES`) are automatically set, along with a sensible default for parallelization.
3. **Ingress Setup**: Enable an ingress to expose vLLM’s HTTP endpoint for external access.
4. **Integration with Hugging Face**: You can pass your Hugging Face token via an environment variable to pull private models.

***

#### Parameter Descriptions

The following parameters can be set with Apolo’s CLI (`apolo run --pass-config ... install ... --set <key>=<value>`). Many are optional but can be used to customize your deployment:

| **Parameter**                     | **Type**  | **Description**                                                                                                                                   |
| --------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **app\_name**                     | String    | Required. Name for your vLLM application (Kubernetes release name, etc.). Must follow Kubernetes naming rules. Example: `llm-inference qwen-32b`. |
| **preset\_name**                  | String    | Required. Apolo preset for resources. E.g. `gpu-xlarge`, `H100X1`, `mi210x2`. Sets CPU, memory, GPU count, and GPU provider.                      |
| **model.modelHFName**             | String    | Required. Hugging Face model repo name. Example: `Qwen/QwQ-32B-preview`.                                                                          |
| **model.modelRevision**           | String    | Optional. Specify the model revision/tag. Example: `main`.                                                                                        |
| **env.HUGGING\_FACE\_HUB\_TOKEN** | String    | Optional. HF token for private model downloads. If left blank, only public models are accessible.                                                 |
| **ingress.enabled**               | Boolean   | Optional (default: `false`). Enables external access to the vLLM HTTP endpoint with a Kubernetes Ingress. Example: `true`.                        |
| **ingress.clusterName**           | String    | Optional. The cluster name used in the generated domain. Example: `novoserve`. Produces `<app_name>.apps.novoserve.org.neu.ro`.                   |
| **serverExtraArgs**               | String\[] | Optional. Additional arguments passed to the `vllm serve` command (e.g. `--dtype=half`, `--max-model-len=131072`).                                |

Any additional chart values can also be provided through `--set` flags, but the above are the most common.

#### Example Apolo CLI Command

Below is a streamlined example command that deploys **vLLM** using the [`app-llm-inference` ](https://github.com/neuro-inc/app-llm-inference)app that deploys to a Nvidia preset:

```bash
apolo run --pass-config ghcr.io/neuro-inc/app-deployment -- \
  install https://github.com/neuro-inc/app-llm-inference \
  llm-inference vllm-large charts/llm-inference-app \
  --timeout=30m \
  --set "preset_name=H100X2" \
  --set "model.modelHFName=Qwen/QwQ-32B-preview" \
  --set "model.modelRevision=main" \
  --set "env.HUGGING_FACE_HUB_TOKEN=<YOUR_HF_TOKEN>" \
  --set "ingress.enabled=true" \
  --set "ingress.clusterName=<YOUR_CLUSTER_BAE>" \
  --set "serverExtraArgs[0]=--dtype=half" \
  --set "serverExtraArgs[1]=--max-model-len=131072" \
  --set "serverExtraArgs[2]=--enforce-eager"
```

Below is a streamlined example command that deploys **vLLM** using the [`app-llm-inference` ](https://github.com/neuro-inc/app-llm-inference)app that deploys to an AMD preset:

```bash
apolo run --pass-config ghcr.io/neuro-inc/app-deployment -- \
  install https://github.com/neuro-inc/app-llm-inference \
  llm-inference vllm-large charts/llm-inference-app \
  --timeout=30m \
  --set "preset_name=mi210x2" \
  --set "model.modelHFName=Qwen/QwQ-32B-preview" \
  --set "model.modelRevision=main" \
  --set "env.HUGGING_FACE_HUB_TOKEN=<YOUR_HF_TOKEN>" \
  --set "ingress.enabled=true" \
  --set "ingress.clusterName=<YOUR_CLUSTER_BAE>" \
  --set "serverExtraArgs[0]=--dtype=half" \
  --set "serverExtraArgs[1]=--max-model-len=131072" \
  --set "serverExtraArgs[2]=--enforce-eager"
```

**Explanation**:

* **`preset_name=gpu-xlarge`** requests 2 GPUs (NVIDIA H100). Apolo automatically sets `CUDA_VISIBLE_DEVICES=0,1` and default parallelization flags unless overridden.
* **`preset_name=mi210x2`** requests 2 GPUs (AMD MI210). Apolo automatically sets `HIP_VISIBLE_DEVICES=0,1` , `ROCR_VISIBLE_DEVICES=0,1`  and default parallelization flags unless overridden.
* **`model.modelHFName=Qwen/QwQ-32B-preview`**: The Hugging Face model to load.
* **`ingress.enabled=true`** & **`ingress.clusterName=<YOUR_CLUSTER_NAME>`**: Creates a public domain (e.g. `vllm-large.apps.<YOUR_CLUSTER_NAME>.org.neu.ro`) pointing to the vLLM deployment.
* **`serverExtraArgs[...]`**: Additional flags (`--dtype=half`, `--max-model-len=131072`, etc.) are appended to the `vllm serve` command.

#### References

* [vLLM Official GitHub Repo](https://github.com/vllm-project/vllm)
* [app-llm-inference Helm Chart Repository](https://github.com/neuro-inc/app-llm-inference)
* [Apolo Documentation](https://docs.apolo.us/apolo-cli/commands/shortcuts#usage-16) (for the usage of `apolo run` and resource presets)
* [Hugging Face Model Hub](https://huggingface.co/) (for discovering or hosting models)




---
File: /docs/apolo-console/apps/available-apps/llm-inference/vllm-inference-details.md
---

# vLLM Inference details

### Under the Hood

When you specify a multi-GPU preset (like a preset with multiple Nvidia and AMD GPUs), **LLM Inference**:

1. **Determines GPU Provider & Count**
   * AMD MI210 → `gpuProvider=amd`, 2 GPUs.
   * NVIDIA → `gpuProvider=nvidia`, 2 GPUs.
2. **Sets GPU Visibility**
   * On AMD: `HIP_VISIBLE_DEVICES=0,1`, `ROCR_VISIBLE_DEVICES=0,1` (if 2 GPUs).
   * On NVIDIA: `CUDA_VISIBLE_DEVICES=0,1`.
3. **Applies a Default Parallel** arguments (e.g. `--tensor-parallel-size=2`) if the user hasn’t already done so.

#### Environment Variables for AMD

By default, if you select a preset with AMD GPU cards, the chart’s logic sets:

* **`HIP_VISIBLE_DEVICES=0,1...`** and **`ROCR_VISIBLE_DEVICES=0,1...`**` ``depending on number of available GPUs:` Tells ROCm which GPUs are accessible.
* **`TORCH_USE_HIP_DSA=1`**: Enables direct storage access for HIP.
* **`HSA_FORCE_FINE_GRAIN_PCIE=1`** & **`HSA_ENABLE_SDMA=1`**: Improves GPU ↔ Host & GPU ↔ GPU memory transfers.
* **`ROCM_DISABLE_CU_MASK=0`**: All compute units remain active.
* **`VLLM_WORKER_MULTIPROC_METHOD=spawn`**: Avoids “fork” issues on AMD.
* **`NCCL_P2P_DISABLE=0`**: By default, we assume your cluster has correct kernel parameters for GPU–GPU direct memory access. If not, you can pass `--set envAmd.NCCL_P2P_DISABLE=1` to forcibly disable P2P.

### Final Notes

* **NCCL / RCCL** logs will appear in the vLLM container logs. Look for lines referencing peer-to-peer if you see a hang.
* On AMD, if you do have persistent hangs, append `--set "envAmd.NCCL_P2P_DISABLE=1"` to your Apolo command to force fallback GPU communication.&#x20;
* For the best performance, we keep ROCm version 6.2+ or 6.3+ in sync with your Docker image (`rocm/vllm-ci`)&#x20;

By combining the right Apolo preset, environment variables, you can reliably run **vLLM** on multiple GPUs—be they AMD or NVIDIA —and get high token throughput for large LLMs.



---
File: /docs/apolo-console/apps/available-apps/apolo-deploy.md
---

# Apolo Deploy




---
File: /docs/apolo-console/apps/available-apps/dify.md
---

# Dify

Dify is an open-source development platform designed for building, managing, and deploying applications powered by large language models (LLMs). Dify provides an intuitive interface that combines essential features such as AI workflow, Retrieval-Augmented Generation (RAG) pipelines, agent-based capabilities, model management, and observability tools, all of which help users transition quickly from prototype to production.

### Key Features

* **AI Workflow Management:** Streamlines the end-to-end development process for LLM apps.
* **RAG Pipelines and Agent Capabilities:** Supports Retrieval-Augmented Generation and agent functionality to handle complex data queries and automate tasks.
* **Model Management:** Enables efficient model management for various LLM deployments.
* **Observability:** Provides tools to monitor and improve app performance in real time.

### Installation and Deployment

You can deploy Dify using the Apolo, which facilitates Helm chart deployment and integrates with other applications running on Apolo, such as Postgres clusters, for seamless data handling.

The installation process automates:

1. Integration with existing PGVector app
2. Dify configs to persist datasets objects at [Apolo Buckets](../pre-installed/buckets.md)
3. Web interface ingress configuration

#### Parameter Descriptions

| Parameter                          | Type    | Description                                                                                                      |
| ---------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| `api.replicas`                     | Integer | Number of API service replicas (default: 1).                                                                     |
| `api.preset_name`                  | String  | Required. CPU/memory preset for the API service (e.g., `cpu-small`).                                             |
| `worker.replicas`                  | Integer | Number of worker service replicas (default: 1).                                                                  |
| `worker.preset_name`               | String  | Required. CPU/memory preset for worker service (e.g., `cpu-small`).                                              |
| `proxy.preset_name`                | String  | Required. CPU/memory preset for the proxy service.                                                               |
| `web.replicas`                     | Integer | Number of web service replicas (default: 1).                                                                     |
| `web.preset_name`                  | String  | Required. CPU/memory preset for the web service.                                                                 |
| `redis.master.preset_name`         | String  | Required. CPU/memory preset for Redis master instance.                                                           |
| `externalPostgres.platformAppName` | String  | Required. PGVector app name to integrate with the Dify app.                                                      |
| `externalPostgres.username`        | String  | Optional. Username within the PGVector app (first available user used if not specified).                         |
| `externalPostgres.dbName`          | String  | Optional. Database to use within the PGVector app (first available DB used if not specified).                    |
| `externalPgvector.platformAppName` | String  | Required. PGVector app name for direct vector data integration. Note: it could be the same externalPostgres app. |
| `externalPgvector.username`        | String  | Optional. Username for PGVector integration (first available user used if not specified).                        |
| `externalPgvector.dbName`          | String  | Optional. Database to use within PGVector for vector data storage.                                               |

This setup uses Helm chart for flexible and scalable deployment, enabling seamless integration with PostgreSQL and PGVector services. Adjust parameters based on your infrastructure requirements and previously installed Postgres app names.

After the installations, users could also integrate LLM inference and embeddings apps to this app. This part of documentation is under development

### References

* [Dify helm chart documentation](https://github.com/neuro-inc/dify-helm)
* [Dify platform documentation](https://docs.dify.ai/)



---
File: /docs/apolo-console/apps/available-apps/fooocus.md
---

# Fooocus

Fooocus is a free, offline, open-source image generator designed for high-quality text-to-image creation with minimal prompt engineering or parameter tuning. It features advanced capabilities like custom inpainting and outpainting algorithms, image prompting, and prompt weighting, ensuring superior results even with simple prompts. Fooocus supports SDXL models, offers robust options for image upscaling and variation, and includes tools for negative prompts, face swapping, and textual image descriptions. Additional features like adjustable style, quality, and sampling parameters, along with multi-prompt and embedding support, make it versatile for creative applications. With a minimum GPU requirement of 4GB, it balances accessibility with powerful functionality.

### Key Features

* **High-Quality Text-to-Image Generation**
  * Requires minimal prompt engineering or parameter tuning.
  * Supports prompts ranging from simple phrases to detailed descriptions (up to 1000 words).
* **Image Upscaling and Variations**
  * Options for upscaling (1.5x, 2x) or creating subtle/strong variations.
* **Inpainting and Outpainting**
  * Custom algorithms and models for enhanced results compared to standard SDXL methods.
* **Image Prompt Support**
  * Unique algorithm for better quality and prompt understanding compared to standard methods.
* **Advanced Features**
  * Style options, guidance settings, quality adjustments, and aspect ratio controls.
* **Multi-Prompt Support**
  * Enables multiple lines of prompts and prompt weighting (e.g., `I am (happy:1.5)`).
  * Includes reweighting algorithms for compatibility with popular prompt formats like A1111.
* **Negative Prompts**
  * Allows specifying what should be avoided in the generated images.
* **Face Swapping**
  * Uses InsightFace for advanced face swap functionality.
* **Image Descriptions**
  * Generate textual descriptions from input images.
* **Support for SDXL Models**
  * Compatible with SDXL models from platforms like Civitai.
* **Custom Sampling Parameters**
  * Fine-tune output with adjustable contrast, sharpness, and other parameters.
* **ControlNet Integration**
  * User-friendly interface for advanced input image controls.
* **Prompt Embedding Support**
  * Use embeddings directly within prompts for precise control.
* **Batch Image Generation**
  * Easily generate multiple images by specifying the desired quantity.

### Installation and Deployment

You can deploy Fooocus using Apolo Flow, which facilitates application chart deployment and integrates with other applications running on Apolo.

The installation process automates:

1. Application deployment in cluster
2. Fooocus configs to persist outputs in Apolo Files
3. Web interface ingress configuration

#### Parameter Descriptions

| Parameter     | Type   | Description                                                          |
| ------------- | ------ | -------------------------------------------------------------------- |
| `preset_name` | String | Required. CPU/GPU/memory preset for theapplication (e.g., `a100x1`). |



### References

* [Fooocus documentation](https://github.com/neuro-inc/Fooocus)
* [Fooocus installation with Apolo Flow documentation](https://github.com/neuro-inc/Fooocus/blob/apolo/APOLO.md)



---
File: /docs/apolo-console/apps/available-apps/jupyter-lab.md
---

# Jupyter Lab




---
File: /docs/apolo-console/apps/available-apps/jupyter-notebook.md
---

# Jupyter Notebook

The Jupyter Notebook application in Apolo Console provides an interactive environment for writing, running, and sharing code in multiple programming languages. It enables users to create dynamic documents that include live code, equations, visualizations, and narrative text, making it a powerful tool for data science, research, and software development.

## Installing Jupyter Notebook

1. In the Apps section, click on Jupyter Notebook to proceed with installation.
2. Configure Resources:
* Select a *Preset* that defines the allocated compute resources (CPU, memory, GPU).
* Enter a unique *App Name* to identify your instance of Jupyter Notebook.
3. Click the Install App button to deploy Jupyter Notebook in your project.

![Jupyter Notebook installation](/docs/.gitbook/assets/console_screenshots/Jupyter-notebook.png)


## Managing Jupyter Notebook
Once installed, the Jupyter Notebook instance can be accessed through the Apolo Console. Navigate to the Apps section to view and manage running instances.
Further details about the Jupyter Notebook setup and usage also are available in the *README.ipynb* file within the notebook environment.

![Jupyter instances](/docs/.gitbook/assets/console_screenshots/Jupyter_instances.png)

### Automatic Shutdown
The installed instance is automatically shut down after 2 hours of inactivity (if no one interacts with it and there are no running cells).
To keep the instance running, ensure that code execution is active and that the session remains interactive.



---
File: /docs/apolo-console/apps/available-apps/ml-flow.md
---

# ML Flow




---
File: /docs/apolo-console/apps/available-apps/postgre-sql.md
---

# PostgreSQL

PostgreSQL is a powerful, open-source relational database system known for its reliability, feature richness, and extensibility. It supports advanced SQL compliance, transactional integrity, and scalability, making it a popular choice for both OLTP and OLAP workloads. PostgreSQL’s flexibility allows for use across a wide range of applications, from web services to large-scale data platforms.Apolo uses the **Crunchy Data distribution of PostgreSQL**, which builds on the core database engine by adding production-grade features such as high availability, automated backups, Kubernetes-native deployment, and enhanced monitoring. This ensures that PostgreSQL on Apolo is robust, secure, and ready for mission-critical workloads in modern cloud environments.

#### Key Features <a href="#key-features" id="key-features"></a>

* **Enterprise-Grade PostgreSQL**: Fully open-source and compliant with PostgreSQL, offering advanced tooling and support for critical workloads.
* **High Availability**: Built-in support for HA via Patroni, Kubernetes-native failover handling, and synchronous streaming replication.
* **Automated Backups & Point-in-Time Recovery (PITR)**: Integrated tools for automated scheduled backups, WAL archiving, and recovery to any point.
* **Monitoring & Metrics**: Native integration with Prometheus and Grafana for visibility into database performance and health.
* **Security & Compliance**: Includes features such as TLS encryption, role-based access control, audit logging, and SELinux hardening.
* **Kubernetes-Native**: Optimized for Kubernetes through Crunchy Data’s PostgreSQL Operator (PGO), enabling declarative management and scalable deployments.

#### Installation and Deployment on Apolo <a href="#installation-and-deployment-on-apolo" id="installation-and-deployment-on-apolo"></a>

You can deploy Crunchy Postgres using an App interface

**Highlights of the Apolo Installation Flow:**

* **Preset-Based Deployment**: Select a suitable Apolo preset (e.g. `cpu-medium`, `cpu-large`) that defines CPU, memory, and storage requirements.
* **Persistent Storage Management**: Automatically provisions high-performance, durable storage with snapshot and backup support.
* **Secrets & Credentials Injection**: Securely injects environment variables and secrets such as `POSTGRES_PASSWORD`, `PGDATA`, and SSL keys.
* **Ingress Configuration**: Easily expose your PostgreSQL instance using an ingress or internal service, depending on access needs.
* **Backup & PITR Support**: Integrates with Apolo’s backup system for regular snapshots and point-in-time recovery options.
* **Observability**: Exposes key PostgreSQL metrics via built-in exporters for monitoring via Apolo’s observability stack or your own Prometheus instance.

***

#### Parameter Descriptions:

The following parameters can be set with Apolo’s CLI&#x20;

(`apolo run --pass-config ... install ... --set <key>=<value>`).

Mainly parameters for the Instances and PgBouncer.&#x20;

**PgBouncer** sits between your application and PostgreSQL, managing and reusing database connections to reduce overhead and improve performance—especially in high-concurrency environments.

| Parameter                   | Type   | Description                                                                                                          |
| --------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| **instanceReplicas**        | Int    | Required. Number of PostgreSQL instances deployed.                                                                   |
| **pgBouncerReplicas**       | Int    | Required. Number of PgBouncer instances deployed.                                                                    |
| **preset\_name**            | String | Required. Apolo preset for resources. E.g. `cpu-large`,`cpu-medium` . Sets CPU, memory, GPU count, and GPU provider. |
| **bouncer\_preset\_name**   | String | Required. Apolo preset for pgBouncer. E.g. `cpu-large`,`cpu-medium` . Sets CPU, memory, GPU count, and GPU provider. |
| **users\[N].name**          | String | Optional. Username to access the database later on.                                                                  |
| **users\[N].databases\[N]** | String | Optional. Database created and given access to specific user.                                                        |

Any additional chart values can also be provided through `--set` flags, but the above are the most common.

#### Example Apolo CLI Command

Below is a streamlined example command that deploys **Postgres** using the [`postgres-app`](https://github.com/neuro-inc/app-llm-inference)

```
  apolo run \
  --pass-config \
  --entrypoint "./entrypoints/pgo.sh install postgresql pgv \
  --set 'instanceReplicas=2' --set 'pgBouncerReplicas=2' \
  --set 'preset_name=cpu-large' \
  --set 'bouncer_preset_name=cpu-large' \
  --set 'users[0].name=myuser' --set 'users[0].databases[0]=mydb'" \
  ghcr.io/neuro-inc/app-deployment
```

### References:

* [Crunchy Postgres Apolo Chart Repository](https://github.com/neuro-inc/app-crunchy-postgres)
* [Crunchy Data Postgres Documentation](https://access.crunchydata.com/documentation/postgres-operator/latest/quickstart)
* [Apolo Documentation](https://docs.apolo.us/apolo-cli/commands/shortcuts#usage-16) (for the usage of `apolo run` and resource presets)



---
File: /docs/apolo-console/apps/available-apps/py-charm.md
---

# PyCharm Community Edition




---
File: /docs/apolo-console/apps/available-apps/README.md
---

# Available apps

| App name                                                  | Description                                                                                                                                                                                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Terminal](terminal.md)                                   | A web-based remote shell instrumented with Apolo CLI, providing immediate access to dedicated compute resources.                                                                                                                                   |
| [LLM Inference](llm-inference/)                           | A highly-available LLM inference service with an OpenAI-compatible API, capable of efficiently serving both standard and quantized models available on HuggingFace.                                                                                |
| [PostgreSQL](postgre-sql.md)                              | An industry-standard relational database system that includes pgvector for advanced semantic search capabilities.                                                                                                                                  |
| [Text Embeddings Inference](text-embeddings-inference.md) | Text Embeddings Inference (TEI) is a comprehensive toolkit designed for efficient deployment and serving of open source text embeddings models. It enables high-performance extraction for the most popular models.                                |
| [Jupyter Notebook](jupyter-notebook.md)                   | An interactive tool that enables the creation and sharing of documents with live code, visualizations, and narrative text.                                                                                                                         |
| [Jupyter Lab](jupyter-lab.md)                             | An interactive development environment designed for managing notebooks, code, and data, enabling seamless creation and sharing of dynamic documents.                                                                                               |
| [VS Code](vs-code.md)                                     | A lightweight, powerful source code editor with a rich ecosystem of extensions for many languages and runtimes.                                                                                                                                    |
| [PyCharm Community Edition](py-charm.md)                  | A Python IDE for data science and web development.                                                                                                                                                                                                 |
| [ML Flow](ml-flow.md)                                     | A tool that streamlines the full lifecycle of machine learning projects, enhancing manageability, traceability, and reproducibility.                                                                                                               |
| [Apolo Deploy](apolo-deploy.md)                           | A simple model deployment service leveraging Triton and MLflow as its core inference servers.                                                                                                                                                      |
| [Dify](dify.md)                                           | Open-source LLM app development platform                                                                                                                                                                                                           |
| [Weaviate](weaviate.md)                                   | A robust, open-source vector database enabling semantic search. Store and query data based on meaning using its GraphQL, REST, and gRPC APIs for seamless integration with your applications. Supports various modules for extended functionality. |
| [Fooocus](fooocus.md)                                     | Fooocus is a free, offline, open-source image generator that creates images from prompts without manual tweaking, requiring minimal GPU memory (4GB).                                                                                              |
| [Stable Diffusion](stable-diffusion.md)                   | Open-source image generation and editing platform powered by advanced latent diffusion models.                                                                                                                                                     |



---
File: /docs/apolo-console/apps/available-apps/stable-diffusion.md
---

# Stable Diffusion

Stable Diffusion is a state-of-the-art deep learning model designed for generating high-quality images from textual descriptions. It utilizes a **latent diffusion process**, a type of generative model that iteratively refines noise to produce detailed and realistic images. This model is highly efficient, scalable, and capable of running on consumer-grade hardware, making it widely used for applications in art generation, content creation, and research. Developed with open accessibility in mind, Stable Diffusion empowers developers and creators to explore generative AI while maintaining adaptability for various use cases.

Apolo utilizes [Stable Diffusion Web UI by AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and [StableStudio UI ](https://github.com/Stability-AI/StableStudio)to make inference/have a UI playground.

Stable Diffusion WebUI is an intuitive, browser-based interface designed for generating and managing AI-generated images using Stable Diffusion. It offers customizable workflows, advanced image settings, and integrations for various Stable Diffusion models, enabling users to create and edit images with ease.

StableStudio is a web application built to enhance the Stable Diffusion experience. It provides minimalistic UI and batch inference capability.

**Key Features**&#x20;

* **API exposure:** Access Stable Diffusion models via RESTful APIs for seamless integration with other applications.&#x20;
* **User-Friendly Interface:** Both platforms feature easy-to-navigate interfaces for AI image generation.&#x20;
* **Customizability:** Fine-tune image outputs using adjustable parameters like prompt strength, resolution, and style preferences.&#x20;
* **Multimodal Integration:** Generate images from text prompts, sketches, or existing images with advanced control over results.&#x20;
* **Batch Processing:** Automate workflows for generating or editing multiple images simultaneously.

### Installation and deployment on Apolo

You can deploy Stable Diffusion WebUI using Apolo, which facilitates Helm chart deployment and integrates with other applications running on the platform. This simplifies deployment and management, allowing for easy customization and integration with your existing infrastructure.

Apolo deploys HuggingFace models.

**The Apolo installation process automates:**&#x20;

* **Dockerization of inference server:** Inference Server is wrapped into Docker container which is supported by Apolo.&#x20;
* **Resource Allocation:** Define resource limits (CPU, memory, GPU) using Apolo presets.&#x20;
* **Persistent Storage:** Automatically provisions persistent storage for your Stable Diffusion data.
* **Ingress Configuration:** Configure ingress for external access to Weaviate's APIs.&#x20;

You can deploy Stable Diffusion WebUI in 2 ways:

**Apolo Console (recommended way)**

<figure><img src="../../../../../.gitbook/assets/image (258).png" alt=""><figcaption><p>Apolo console with SD</p></figcaption></figure>

**Apolo Cli**

```
apolo run --pass-config ghcr.io/neuro-inc/app-deployment -- install https://github.com/neuro-inc/app-stable-diffusion \
  stable-diffusion stable-studio charts/app-stable-diffusion \
  --timeout=900s \
  --dependency-update \
  --set "api.replicaCount=1" \  # optional, int
  --set "api.ingress.enabled=true" \ # optional, str, default=true
  --set "api.env.HUGGING_FACE_HUB_TOKEN=YOUR_TOKEN" \ # required, (Huggingface hub token https://huggingface.co/docs/hub/en/security-tokens)
  --set "preset_name=YOUR_PRESET" \ # required, str, (It is recommended to use GPU-accelerated machines)
  --set "stablestudio.enabled=true" \  # required, str (default=true)  (If you want to enable StableStudio UI playground)
  --set "stablestudio.preset_name=cpu-large" \ # if stablestudio.enabled=true, then required
  --set "model.modelHFName=stabilityai/stable-diffusion-2" \  # required, str (Huggingface model name, Example: stabilityai/stable-diffusion-2)
  --set "model.modelFiles=768-v-ema.safetensors" \  # optional, str, (Huggingface model files, model weights, comma-separated Example: 768-v-ema.safetensors)

```

### Parameters descriptions

| Parameter                        | Type    | Description                                                                                                                                         |
| -------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api.replicaCount`               | Integer | Optional. Number of instances. Default is 1                                                                                                         |
| `preset_name`                    | String  | Required. CPU/GPU/memory preset for the application (e.g., `a100x1`).                                                                               |
| `api.env.HUGGING_FACE_HUB_TOKEN` | String  | Required. HuggingFace token so we can pull the model                                                                                                |
| `api.ingress.enabled`            | String  | Required. If you want to expose ingress in your app.                                                                                                |
| `stablestudio.enabled`           | String  | Required. If you want to expose StableStudio UI as part of your deployment                                                                          |
| `stablestudio.preset_name`       | String  | Required. If you enabled StableStudio deployment                                                                                                    |
| `model.modelHFName`              | String  | Required. Name of the HuggingFace model (e.g. `stabilityai/stable-diffusion-2` ).                                                                   |
| `model.modelFiles`               | String  | Optional. Comma Separated list of particular model files that you will use. For example only `*.safetensors` file, so we don't pull all repository. |





### API usage&#x20;

After you application is installed, you can utilize the WebUI or API endpoints exposed

**Swagger API documentation:**&#x20;

https://\<APP\_HOST>>/docs&#x20;

**txt2img API endpoint:** https://\<APP\_HOST>/sdapi/v1/txt2img&#x20;

**Request example:**

```
curl -X 'POST' \
  'https://<APP_HOST>/sdapi/v1/txt2img' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Some prompt"
}'
```

### Integration with StableStudio

When your stable diffusion application is exposed, and if you deployed with StableStudio \
You can utilize StableStudio WebUI

Click settings on the right corner of your StableStudio WebUI

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-02-04 at 15.45.24.png" alt=""><figcaption></figcaption></figure>

Paste external url for your stable diffusion webui HOST Url\
The status should be "Ready without history plugin"

Note: Url is persisted only on localStorage, so if you share StableStudio, it needs to be configured again\


<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-02-04 at 15.53.53.png" alt=""><figcaption></figcaption></figure>

Now click Generate and enjoy StableStudio UI

### References

* [StableDiffusion repository](https://github.com/Stability-AI/StableDiffusion)
* [Stable diffusion webui Automatic repository](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
* [StableStudio repository](https://github.com/Stability-AI/StableStudio)



---
File: /docs/apolo-console/apps/available-apps/terminal.md
---

# Terminal

The Apolo Terminal app allows users to execute shell commands, manage files, and interact with computational resources directly through a web-based interface. This guide provides step-by-step instructions for accessing, installing, and using the Terminal app.

## Accessing the Terminal App

Navigate to the **Apolo Console** and click on the **Apps** section from the left-hand navigation menu. You will see a list of available apps, as shown in the screenshot below.

![All apps view](/docs/.gitbook/assets/console_screenshots/Terminal_app_1.png)

Locate the **Terminal** app. If it is not yet installed, proceed to the installation steps.

## Installing the Terminal App

1.  Select the **Terminal** app.

    Click on the button **Install** located on the **Terminal** app card.
2.  Configure _resources_.

    After selecting the Terminal app, you will be redirected to the installation page. Under the **Resources** tab, choose a preset configuration based on your computational needs (e.g., `cpu-small`, `cpu-medium`).
3.  Add _metadata_.\
    In the next step, under the **Metadata** tab, provide a name for your app instance.

    ![Terminal configuration](/docs/.gitbook/assets/console_screenshots/terminal_settings.png)
4. Install the App.\
   Click on the **Install App** button to complete the installation process. The app will appear in the **Installed Apps** tab once successfully deployed.

## Managing Installed Terminal Apps

To view and manage installed instances of the Terminal app:

1. Go to the **Installed Apps** tab.
2.  You will see a list of running **Terminal** app instances.

    ![Installed apps](/docs/.gitbook/assets/console_screenshots/terminal_installed.png)

You can look its details by clicking on the button **Details** for each instance.

![Terminal card](/docs/.gitbook/assets/console_screenshots/terminal_card.png)

**Details page** contains the next information:

* Terminal settings (Image name, preset name, preset resources, etc.)
* App status transition
* Telemetry
* Logs
* Outputs values

![Terminal instance details](/docs/.gitbook/assets/console_screenshots/terminal_details.png)

## Using the Terminal App

1.  Launch the **Terminal**.

    Click **Open** button on an instance of the **Terminal** app from the **Installed Apps** list. This will open a web-based shell environment.
2.  Run Commands.\
    Use the terminal to execute shell commands. A welcome message provides helpful examples of commands you can run, such as managing Apolo CLI workflows and running jobs.

    **Example:**

    ```bash
    apolo run alpine:latest echo 'Hello, World!'
    ```

    ![](/docs/.gitbook/assets/console_screenshots/terminal_app.png)

    ![Terminal interface](/docs/.gitbook/assets/console_screenshots/terminal_app2.png)



---
File: /docs/apolo-console/apps/available-apps/text-embeddings-inference.md
---

# Text Embeddings Inference




---
File: /docs/apolo-console/apps/available-apps/vs-code.md
---

# VS Code




---
File: /docs/apolo-console/apps/available-apps/weaviate.md
---

# Weaviate

**Weaviate** is a robust, open-source vector database that allows you to store and query data based on its meaning. It supports various modules for text, image, and multimodal vectorization, enabling semantic search, advanced filtering, and question-answering. Weaviate offers flexible deployment options and integrates seamlessly with popular machine learning models and frameworks, providing **GraphQL**, **REST**, and **gRPC APIs** for easy integration with your applications.

#### **Key Features**

* **Semantic Search**: Store and query data based on semantic meaning, going beyond keyword matching.
* **Modular Architecture**: Extend Weaviate's functionality with various modules for different data types and tasks.
* **High Performance**: Optimized for speed and scalability to handle large datasets and complex queries.
* **Multiple APIs**: **GraphQL**, **REST**, and **gRPC APIs** provide flexible integration options for your applications.
* **Horizontal Scalability**: Easily scale Weaviate to handle growing data and query loads.

#### **Installation and Deployment on Apolo**

You can deploy **Weaviate** using **Apolo**, which facilitates Helm chart deployment and integrates with other applications running on the platform. This simplifies deployment and management, allowing for easy customization and integration with your existing infrastructure.

The Apolo installation process automates:

1. **Resource Allocation**: Define resource limits (CPU, memory, GPU) using Apolo presets.
2. **Persistent Storage**: Automatically provisions persistent storage for your Weaviate data.
3. **Ingress Configuration**: Configure ingress for external access to Weaviate's APIs.
4. **Cluster API Authentication**: Set up authentication for Weaviate's cluster API.
5. **Backups**: Configure backups to an Apolo bucket.

#### **Parameter Descriptions**

The following parameters can be set when deploying Weaviate using the Apolo CLI:

<table data-header-hidden><thead><tr><th width="252"></th><th width="105"></th><th></th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td></tr><tr><td><strong>app_name</strong></td><td>String</td><td>Required. The name of your Weaviate application (used to name Kubernetes resources). Must adhere to Kubernetes naming conventions. Example: <code>weaviate</code>.</td></tr><tr><td><strong>preset_name</strong></td><td>String</td><td>Required. The name of the Apolo preset to use for resource allocation (e.g., <code>cpu-small</code>, <code>gpu-medium</code>). Determines CPU, memory, and GPU resources. Example: <code>cpu-large</code>.</td></tr><tr><td><strong>persistence.size</strong></td><td>String</td><td>Optional (default: <code>32Gi</code>). The size of the persistent volume claim for Weaviate's data. Example: <code>64Gi</code>.</td></tr><tr><td><strong>ingress.enabled</strong></td><td>Boolean</td><td>Optional (default: <code>false</code>). Enables ingress for external access to Weaviate's HTTP and gRPC APIs. Example: <code>true</code>.</td></tr><tr><td><strong>ingress.clusterName</strong></td><td>String</td><td>Optional (default: <code>weaviate</code>). The cluster name for ingress (used in the generated hostname). Only relevant if ingress is enabled. Example: <code>cl1</code>.</td></tr><tr><td><strong>ingress.grpc.enabled</strong></td><td>Boolean</td><td>Optional (default: <code>false</code>). Enable ingress for external access to Weaviate gRPC APIs specifically. Example: <code>true</code>.</td></tr><tr><td><strong>clusterApi.username</strong></td><td>String</td><td>Optional. Username for Weaviate's cluster API. If not specified, it is automatically generated and stored as a secret. Example: <code>taddeus</code></td></tr><tr><td><strong>clusterApi.password</strong></td><td>String</td><td>Optional. Password for Weaviate's cluster API. If not specified, it is automatically generated and stored as a secret. Example: <code>31n81tSIc$7il4Js</code></td></tr><tr><td><strong>authentication.enabled</strong></td><td>Boolean</td><td>Optional (default: <code>false</code>). Enable or disable client authentication. If not set or false, API key authentication must be configured. Example: <code>true</code>.</td></tr><tr><td><strong>backups.enabled</strong></td><td>Boolean</td><td>Optional (default: <code>false</code>). Enable or disable data backups. If enabled, the bucket is created with the name <code>weaviate-backup</code> by default. Example: <code>true</code>.</td></tr></tbody></table>

Embedding modules are not available out of the box; for now, embeddings must be generated externally with an embedding model of your choice and can be saved in Weaviate.

#### **Example Apolo CLI Command**

```bash
apolo run --pass-config ghcr.io/neuro-inc/app-deployment \
  -- install https://github.com/neuro-inc/weaviate-helm weaviate weaviate weaviate \
  --timeout=15m0s \
  --set preset_name=cpu-large \
  --set persistence.size=32Gi \
  --set ingress.enabled=true \
  --set ingress.clusterName=cl1 \
  --set ingress.grpc.enabled=true \
  --set clusterApi.username=taddeus \
  --set clusterApi.password=31n81tSIc$7il4Js \
  --set authentication.enabled=true \
  --set backups.enabled=true
```

#### **Example Python Scripts**

This example demonstrates connecting to **Weaviate**, defining a schema, embedding documents using the **NV-Embed-v2** model, storing them in Weaviate, and performing a similarity search.

```python

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
import weaviate

# Step 1: Connect to Weaviate
client = weaviate.Client(
    url="<your-ingress-endpoint>",
    auth_client_secret=weaviate.AuthApiKey(api_key="<your-cluster-api-password>")
)


if client.is_ready():
    print("Connected to Weaviate!")
else:
    print("Weaviate is not ready.")
    exit(1)

# Step 2: Define a schema class in Weaviate
schema_class = {
    "class": "Document",
    "description": "A collection of documents for testing embeddings",
    "vectorizer": "none",  # We will provide our own vectors
    "properties": [
        {
            "name": "title",
            "description": "Title of the document",
            "dataType": ["text"],
        },
        {
            "name": "content",
            "description": "Content of the document",
            "dataType": ["text"],
        },
    ],
}

# Check if the class already exists
existing_classes = client.schema.get()['classes']
class_names = [c['class'] for c in existing_classes]
if "Document" not in class_names:
    client.schema.create_class(schema_class)
    print("Schema 'Document' created.")
else:
    print("Schema 'Document' already exists.")

# Step 3: Load NV-Embed-v2 model
model_name = "nvidia/NV-Embed-v2"
print("Loading NV-Embed-v2 model...")
model = AutoModel.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
print("Model loaded.")

# Step 4: Prepare a dataset
documents = [
    {
        "title": "The Impact of Climate Change",
        "content": "Climate change affects weather patterns, sea levels, and ecosystems."
    },
    {
        "title": "Artificial Intelligence in Healthcare",
        "content": "AI is revolutionizing diagnostics and treatment plans in healthcare."
    },
    {
        "title": "Advancements in Quantum Computing",
        "content": "Quantum computers use quantum bits to perform complex calculations."
    },
    {
        "title": "Renewable Energy Sources",
        "content": "Solar and wind energy are key to reducing carbon emissions."
    },
    {
        "title": "The Basics of Machine Learning",
        "content": "Machine learning enables computers to learn from data."
    },
    {
        "title": "Ocean Conservation Efforts",
        "content": "Protecting marine life is essential for ecological balance."
    },
    {
        "title": "Blockchain Technology Explained",
        "content": "Blockchain provides a decentralized ledger for transactions."
    },
    {
        "title": "The Human Immune System",
        "content": "The immune system defends the body against infections."
    },
    {
        "title": "Exploring the Solar System",
        "content": "Mars rovers are providing new insights about the red planet."
    },
    {
        "title": "History of the Internet",
        "content": "The internet has transformed communication and information sharing."
    },
]

# Step 5: Generate embeddings for the documents
def generate_embeddings(texts, prefix=""):
    max_length = 32768  # Adjust as needed
    inputs = [prefix + text + tokenizer.eos_token for text in texts]
    with torch.no_grad():
        embeddings = model.encode(inputs, instruction=prefix, max_length=max_length)
    embeddings = F.normalize(embeddings, p=2, dim=1)
    return embeddings

# Since we are encoding documents, no instruction prefix is needed
print("Generating embeddings for documents...")
doc_texts = [doc["content"] for doc in documents]
doc_embeddings = generate_embeddings(doc_texts)
print("Document embeddings generated.")

# Step 6: Store documents and embeddings in Weaviate
print("Adding documents to Weaviate...")
for doc, embedding in zip(documents, doc_embeddings):
    # Convert the embedding tensor to a list
    embedding_list = embedding.tolist()
    # Add the document to Weaviate with the vector
    client.data_object.create(
        data_object=doc,
        class_name="Document",
        vector=embedding_list
    )
print("Documents added to Weaviate.")

# Step 7: Perform a similarity search
query_text = "How does renewable energy help combat climate change?"
query_prefix = "Instruct: Given a question, retrieve passages that answer the question\nQuery: "

print("Generating embedding for the query...")
query_embedding = generate_embeddings([query_text], prefix=query_prefix)[0]
query_embedding_list = query_embedding.tolist()
print("Query embedding generated.")

print("Performing similarity search in Weaviate...")
# Use the 'nearVector' filter to find similar documents
result = (
    client.query
    .get("Document", ["title", "content"])
    .with_near_vector({"vector": query_embedding_list})
    .with_limit(3)
    .do()
)

print("Search results:")
for idx, res in enumerate(result["data"]["Get"]["Document"], start=1):
    title = res.get("title", "No Title")
    content = res.get("content", "No Content")
    print(f"\nResult {idx}:")
    print(f"Title: {title}")
    print(f"Content: {content}")


```

This script demonstrates connecting to **Weaviate**, defining a schema, embedding documents using **OpenAI embeddings**, storing them in Weaviate via **LlamaIndex**, and performing a similarity search.\\

```python
import os
from llama_index.core import (
    VectorStoreIndex, 
    Document, 
    StorageContext,
    ServiceContext
)
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
import weaviate
import openai

os.environ["OPENAI_API_KEY"] = "<your-api-key>"
# Step 1: Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    print("Please set the OPENAI_API_KEY environment variable.")
    exit(1)

# Step 2: Connect to Weaviate using the v3 client
weaviate_url = "<your-ingress-endpoint>"
client = weaviate.Client(url=weaviate_url, auth_client_secret=weaviate.AuthApiKey(api_key="<your-cluster-api-password>"))

if client.is_ready():
    print("Connected to Weaviate!")
else:
    print("Failed to connect to Weaviate!")
    exit(1)

# Step 3: Define schema class in Weaviate
COLLECTION_NAME = "LlamaDocument"  # Using capital letter as required

schema = {
    "class": COLLECTION_NAME,
    "description": "A collection of documents for testing embeddings",
    "vectorizer": "none",  # We will provide our own vectors via OpenAI
    "properties": [
        {
            "name": "title",
            "dataType": ["text"],
            "description": "Title of the document",
        },
        {
            "name": "content",
            "dataType": ["text"],
            "description": "Content of the document",
        },
    ]
}

# Check if the class already exists
existing_classes = client.schema.get()['classes']
class_names = [c['class'] for c in existing_classes]
if COLLECTION_NAME not in class_names:
    client.schema.create_class(schema)
    print(f"Schema '{COLLECTION_NAME}' created.")
else:
    print(f"Schema '{COLLECTION_NAME}' already exists.")

# Step 3.1: Monkey-Patch the class_schema_exists Function
# This is necessary because llama_index's WeaviateVectorStore uses a v3 method that doesn't exist in v4
from llama_index.vector_stores.weaviate.utils import class_schema_exists
import llama_index.vector_stores.weaviate.utils as weav_utils

def new_class_schema_exists(client, class_name):
    return client.schema.contains(class_name)

weav_utils.class_schema_exists = new_class_schema_exists

# Step 4: Prepare the dataset
documents = [
    {
        "title": "The Impact of Climate Change",
        "content": "Climate change affects weather patterns, sea levels, and ecosystems."
    },
    {
        "title": "Artificial Intelligence in Healthcare",
        "content": "AI is revolutionizing diagnostics and treatment plans in healthcare."
    },
    {
        "title": "Advancements in Quantum Computing",
        "content": "Quantum computers use quantum bits to perform complex calculations."
    },
    {
        "title": "Renewable Energy Sources",
        "content": "Solar and wind energy are key to reducing carbon emissions."
    },
    {
        "title": "The Basics of Machine Learning",
        "content": "Machine learning enables computers to learn from data."
    },
    {
        "title": "Ocean Conservation Efforts",
        "content": "Protecting marine life is essential for ecological balance."
    },
    {
        "title": "Blockchain Technology Explained",
        "content": "Blockchain provides a decentralized ledger for transactions."
    },
    {
        "title": "The Human Immune System",
        "content": "The immune system defends the body against infections."
    },
    {
        "title": "Exploring the Solar System",
        "content": "Mars rovers are providing new insights about the red planet."
    },
    {
        "title": "History of the Internet",
        "content": "The internet has transformed communication and information sharing."
    },
    {
        "title": "The Evolution of Space Exploration",
        "content": "Human missions to Mars and beyond are shaping the future of space exploration."
    },
    {
        "title": "The Role of Genetics in Medicine",
        "content": "Genetic research is unlocking personalized treatments and therapies."
    },
    {
        "title": "Cybersecurity in the Digital Age",
        "content": "Protecting sensitive data is critical as cyber threats evolve."
    },
    {
        "title": "The Importance of Mental Health Awareness",
        "content": "Raising awareness about mental health promotes early intervention and support."
    },
    {
        "title": "Breakthroughs in Renewable Energy Storage",
        "content": "Innovative batteries are making renewable energy more reliable."
    },
    {
        "title": "Exploring the Deep Ocean",
        "content": "Underwater exploration reveals new species and ecosystems."
    },
    {
        "title": "The Science of Sleep",
        "content": "Understanding sleep cycles is key to improving health and productivity."
    },
    {
        "title": "The Future of Urban Transportation",
        "content": "Electric vehicles and smart infrastructure are transforming city transit."
    },
    {
        "title": "The Ethics of Artificial Intelligence",
        "content": "AI raises important questions about privacy, fairness, and accountability."
    },
    {
        "title": "The Rise of Virtual Reality",
        "content": "VR is revolutionizing gaming, training, and immersive experiences."
    },
    {
        "title": "The Power of Microorganisms",
        "content": "Microbes play a crucial role in agriculture, medicine, and industry."
    },
    {
        "title": "The History of Renewable Energy",
        "content": "From windmills to solar panels, renewable energy has evolved significantly."
    },
    {
        "title": "Exploring the Arctic",
        "content": "The Arctic holds clues to understanding climate change and global ecosystems."
    },
    {
        "title": "The Impact of Social Media",
        "content": "Social media shapes communication, relationships, and public discourse."
    },
    {
        "title": "The Basics of Cryptocurrency",
        "content": "Cryptocurrencies use blockchain technology for secure digital transactions."
    },
    {
        "title": "The Wonders of Human Brain",
        "content": "Neuroscience is uncovering how the brain processes information and emotions."
    },
    {
        "title": "Innovations in Agriculture",
        "content": "Precision farming and biotechnology are boosting crop yields."
    },
    {
        "title": "Understanding Climate Resilience",
        "content": "Building climate-resilient communities is crucial in adapting to change."
    },
    {
        "title": "The Future of Artificial Intelligence",
        "content": "Advances in AI are shaping industries and daily life."
    },
    {
        "title": "The Mysteries of Black Holes",
        "content": "Black holes challenge our understanding of physics and the universe."
    },
    {
        "title": "The Secrets of Ancient Civilizations",
        "content": "Archaeological discoveries reveal insights into ancient cultures and traditions."
    },
    {
        "title": "The Role of Nanotechnology in Medicine",
        "content": "Nanotechnology is enabling precise drug delivery and advanced treatments."
    },
    {
        "title": "The Impact of 5G Technology",
        "content": "5G networks are transforming communication and powering IoT advancements."
    },
    {
        "title": "Renewable Energy in Urban Planning",
        "content": "Cities are integrating solar and wind energy to promote sustainability."
    },
    {
        "title": "The Psychology of Motivation",
        "content": "Understanding intrinsic and extrinsic motivation can enhance personal achievement."
    },
    {
        "title": "The Importance of Biodiversity",
        "content": "Diverse ecosystems are vital for maintaining balance in nature."
    },
    {
        "title": "The Science of Artificial Photosynthesis",
        "content": "Artificial photosynthesis holds potential for renewable energy production."
    },
    {
        "title": "Advances in Autonomous Vehicles",
        "content": "Self-driving technology is reshaping transportation and logistics."
    },
    {
        "title": "The History of Electric Cars",
        "content": "Electric vehicles have evolved from early prototypes to modern innovations."
    },
    {
        "title": "Exploring Exoplanets",
        "content": "Scientists are discovering Earth-like planets in distant solar systems."
    },
    {
        "title": "The Future of Food Technology",
        "content": "Lab-grown meat and vertical farming are addressing global food demands."
    },
    {
        "title": "The Importance of Water Conservation",
        "content": "Efficient water use is essential to combat scarcity and climate change."
    },
    {
        "title": "The Evolution of Artificial Intelligence",
        "content": "AI has progressed from simple algorithms to advanced machine learning."
    },
    {
        "title": "The Physics of Gravitational Waves",
        "content": "Gravitational waves provide a new way to observe cosmic events."
    },
    {
        "title": "The Role of STEM Education",
        "content": "STEM programs prepare students for careers in science and technology."
    },
    {
        "title": "The Ethics of Genetic Engineering",
        "content": "CRISPR technology raises questions about the future of genetic modification."
    },
    {
        "title": "Renewable Energy in Developing Countries",
        "content": "Solar and wind projects are transforming energy access in remote areas."
    },
    {
        "title": "The Search for Dark Matter",
        "content": "Physicists are investigating the mysterious substance that shapes the universe."
    },
    {
        "title": "The Role of Artificial Intelligence in Finance",
        "content": "AI is improving fraud detection, trading strategies, and financial planning."
    },
    {
        "title": "The Impact of Climate Activism",
        "content": "Grassroots movements are driving policy changes and awareness on climate issues."
    }
]

# Convert to llama_index Documents
documents_list = [
    Document(
        text=doc["content"],
        metadata={"title": doc["title"]}
    )
    for doc in documents
]

# Step 5: Set up the embedding model
embed_model = OpenAIEmbedding(
    model="text-embedding-ada-002",
    embed_batch_size=10  # Adjust batch size as needed
)

# Step 6: Set up the vector store using WeaviateVectorStore
vector_store = WeaviateVectorStore(
    weaviate_client=client,
    index_name=COLLECTION_NAME,
)

# Step 7: Create the storage and service contexts
storage_context = StorageContext.from_defaults(vector_store=vector_store)
service_context = ServiceContext.from_defaults(embed_model=embed_model)

# Step 8: Build the index and add documents to Weaviate
print("Adding documents to Weaviate...")
index = VectorStoreIndex.from_documents(
    documents_list,
    storage_context=storage_context,
    service_context=service_context
)
print("Documents added to Weaviate.")

# Step 9: Perform a similarity search
query_text = "How does renewable energy help combat climate change?"

print("Performing similarity search in Weaviate...")
# Perform the query using the query engine
query_engine = index.as_query_engine(top_k=5)
response = query_engine.query(query_text)

# Print the results
print("\nSearch results:")
print(f"Response: {response}")
print("\nSource documents:")
for idx, node in enumerate(response.source_nodes, start=1):
    doc = node.node
    title = doc.metadata.get("title", "No Title")
    content = doc.get_text()
    print(f"\nResult {idx}:")
    print(f"Title: {title}")
    print(f"Content: {content}")

```

#### **References**

* [Weaviate Official Page](https://weaviate.io/)
* [Weaviate Helm Chart Documentation](https://weaviate.io/developers/weaviate/installation/kubernetes)
* [Weaviate Helm Chart Repository](https://github.com/neuro-inc/weaviate-helm)
* [Weaviate Platform Documentation](https://weaviate.io/developers/weaviate)
* [Weaviate Oficial Repository](https://github.com/weaviate/weaviate)



---
File: /docs/apolo-console/apps/pre-installed/jobs/README.md
---

---
description: Apolo workloads
---

# Jobs

## Overview

The **Jobs** App is a tool that allows users to schedule and execute containerized tasks and processes. It provides a user-friendly interface to manage these workloads, simplifying tasks like data processing, model training and inference, and other batch jobs. This app is designed to provide flexibility and control over how these jobs are run, while offering monitoring features for insights and debugging. Key features of the Jobs App include:

* **Containerized Execution:** Jobs are run inside containers, allowing for consistency and portability.
* **Resource Management:** Users can allocate specific CPU, memory, and GPU resources to each job based on presets available in the cluster
* **Flexible Scheduling:** Jobs can be set to run immediately or scheduled for future execution.
* **Monitoring and Logs:** Real-time monitoring, logs, and telemetry allow users to observe the job's performance and troubleshoot issues.

## Running jobs

The Apolo platform offers multiple interfaces to manage jobs: the Web UI, the Command Line Interface (CLI), and a Python SDK. This guide will explaining the process of creating jobs via the Web UI. To learn more about running jobs using Apolo CLI, visit the Apolo CLI [Jobs app page](../../../../../cli/apps/jobs.md).

### Using the Web UI

#### Steps

1.  **Navigate to the Jobs App:**

    * From the main page, go to the left-hand menu.
    * Click on the "Jobs" option in the left hand menu. This will open the Jobs dashboard.

    ![](../../../../.gitbook/assets/jobs-1.png)
2.  **Initiate Job Creation:**

    * In the Jobs dashboard, click the "Create New Job" button. This will bring you to the "Create New Job" form.

    ![](../../../../.gitbook/assets/jobs-2-cropped.png)
3.  **Configure Job Details**

    * The job creation form has seven steps: Image, Resources, Integrations, Networking, Metadata, Scheduling and Advanced

    ![](../../../../.gitbook/assets/jobs-3.png)

    * **Image:**
      * **Image Name:** Enter a name for your job's image, for instance, "python/latest".
      * **Entrypoint:** Specify the command that will execute in the container when your job runs. For example: python -m http.server 4567.\
        Note: You can also set other configurations in this section if necessary like command, Working Directory, and Environment Variables.
    * **Resources:**
      * **Preset:** Click on the dropdown menu labeled 'Preset'.
      * Choose a preset for your job by selecting it from the popup. Preset determines the compute resources allocated to the job. For example, cpu-medium.
      * Click Apply to select the preset.\
        Note: You can add Volumes to the Job in this step.
    * **Integrations:**
      * Connect your job to a MLFlow Server or the Apollo Engine by clicking the corresponding dropdown menus.
    * **Networking:**
      * Configure the HTTP port to expose.\
        Note: You can also configure HTTP authentication in this step.
    * **Metadata:**
      * **Name:** Enter the name you want to give to your job.
      * **Description:** Add an optional description to help understand what your job is for.\
        Note: You can add Tags to the Job in this step.
    * **Scheduling:**
      * **Restart policy**: Pick the behavior that the Job should take if it fails
      * Configure Lifespan, Schedule Timeout, Priority and Wait for jobs quota in this section.
    * **Advanced**
      * Set more specific settings for the Job, like Request extended "/dev/shm" space, Launch the job in a privileged mode, and Allocate TTY.
4. **Submit the Job:**
   * Once you have configured all the necessary details, click the "Submit New Job" button at the bottom of the form. This submits the job to the queue for scheduling.
5.  **Monitor Job Status:**

    * After submitting, you'll be redirected to the job's detail page.

    ![](../../../../.gitbook/assets/jobs-4.png)

    * The job starts in Pending state.
    * The status will change during its execution from Pending, to Running and finally to Succeeded or Failed.
    * You can view the logs, telemetry, and details in the corresponding tabs.
6.  **Access Job Output**

    * Click the Open button to access the Job output from a browser.\
      Note: You can view Status transition in the Observability tab to check the state of the Job at specific times.\
      Note: You can also Save Image, Refresh, and Rerun the Job in this screen.

    ![](../../../../.gitbook/assets/jobs-5.png)
7. **Review Jobs**
   * Go back to the Jobs dashboard. Here you can view a list of Jobs, and filter it by status.

To learn more about debugging and monitoring jobs once they are started, visit the [Apolo CLI Jobs app page](../../../../cli/apps/jobs.md#debugging-jobs).

## Reference

* [Apolo CLI job reference](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/job)
* [Apolo Flow live job configuration syntax](https://app.gitbook.com/s/-MMLOF_FqiWBMcOdY8cj/workflow-syntax/live-workflow-syntax#jobs)
* [Apolo Flow batch task configuration syntax](https://app.gitbook.com/s/-MMLOF_FqiWBMcOdY8cj/workflow-syntax/batch-workflow-syntax#tasks)



---
File: /docs/apolo-console/apps/pre-installed/jobs/remote-debugging-with-pycharm-professional.md
---

# Remote Debugging with PyCharm Professional

## Introduction

In this tutorial, you can learn how to set up remote debugging with PyCharm Professional on the platform using the flow template.

{% hint style="warning" %}
Remote debugging relies on a running SSH server in a job's 22 port. We ensure it for you if you use our base image (`ghcr.io/neuro-inc/base`).
{% endhint %}

## Initializing a new flow

First, make sure that you have the Apolo CLI client and [**cookiecutter**](https://github.com/cookiecutter/cookiecutter) installed and configured, refer to [getting-started.md](../../../../../../apolo-console/first-steps/getting-started.md#installing-the-cli "mention")

Then, initialize a new flow:

```bash
$ cookiecutter gh:neuro-inc/cookiecutter-neuro-project --checkout release
```

This command will prompt you to enter some info about your flow:

```
project_name [Name of the project]: Apolo PyCharm
project_dir [apolo pycharm]:
project_id [apolo_pycharm]:
code_directory [modules]:
preserve Neuro Flow template hints [yes]:
```

Next, switch to the new project's folder and configure the project's environment on the Platform:

```bash
$ cd apolo_pycharm 
$ apolo-flow build train
```

## Setting up PyCharm

Open the project you have just created in PyCharm Professional and add the code you want to debug as a new `main.py` file (in this example, we use a code snippet from the [JetBrains documentation](https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html)).

Then, you will need to exclude all directories that don't contain Python code (in an empty Apolo project, only the `modules` folder will contain code). PyCharm doesn't synchronize excluded directories. Select all directories to exclude, right-click, and select **Mark Directory as** -> **Excluded**. As a result, you will see a configured project:

![](</docs/.gitbook/assets/image (243).png>)

Run these commands to upload your code to the platform storage:

```bash
> apolo-flow mkvolumes
> apolo-flow upload ALL
```

Now, we are ready to start a GPU-powered development job on the platform. Run the following command:

<pre class="language-bash"><code class="lang-bash"><strong>> apolo-flow run remote_debug
</strong></code></pre>

![](</docs/.gitbook/assets/image (249).png>)

This command starts a `remote_debug` job on the platform. This job uses the user's default preset and forwards the local port 2211 to the job's SSH port. All running jobs consume your quota, so please _don't forget to terminate your jobs_ when they are no longer needed. You can use `apolo-flow kill remote_debug` to kill the job you created in the previous step or `apolo-flow kill ALL` to kill all your running jobs.

Then go back to the PyCharm project and navigate to **Preferences** -> **Project** -> **Project interpreter** (you can also search for "interpreter"). Click the **gear icon** to view the project interpreter options and select **Add...** In the new window, select **SSH Interpreter** and set up the following configuration:

* Host: _localhost_
* Port: _2211_
* Username: _root_

![](</docs/.gitbook/assets/image (241).png>)

When this is done, click **Next**.

In the new window, specify the paths for the interpreter and synced folders:

```bash
Interpreter: /usr/bin/python
Sync folders: <Project root> -> /apolo_pycharm
```

Note that, within the job, your project's root folder is available at the root of the filesystem: `/{project_name}` .

Click **Finish,** and your configuration is ready:

![](</docs/.gitbook/assets/image (242).png>)

Click **OK**.

Once you apply the remote interpreter configuration, PyCharm will start file synchronization.

Your PyCharm project is now configured to work with a remote Python interpreter running in a job.

## Debugging

In this example, we're working with the `main.py` file. To enter debug mode, right-click the file and click **Debug 'main'**:

![](</docs/.gitbook/assets/image (233).png>)

Now, you can interact with the file in debug mode:

![](</docs/.gitbook/assets/image (246).png>)

{% hint style="info" %}
If your project's mapping was not configured and the remote interpreter attempts to execute a file with a local path on the remote environment, you might need to specify the path mappings. You can do that at **Run** -> **Edit Configurations...** -> **Path mappings**:
{% endhint %}

![](</docs/.gitbook/assets/image (235).png>)



---
File: /docs/apolo-console/apps/pre-installed/jobs/remote-debugging-with-vs-code.md
---

# Remote Debugging with VS Code

## Introduction

In this tutorial, we will show how to set up remote debugging with VS Code on the platform using the flow template.

{% hint style="warning" %}
Remote debugging relies on a running SSH server in a job's 22 port. We ensure it for you if you use our base image (`ghcr.io/neuro-inc/base`).
{% endhint %}

## Initializing a new project

Make sure you have CLI and [**cookiecutter**](https://github.com/cookiecutter/cookiecutter) installed, refer to [getting-started.md](../../../../../apolo-console/first-steps/getting-started.md "mention") for instructions.

Then, initialize an empty flow:

```bash
$ cookiecutter gh:neuro-inc/cookiecutter-neuro-project --checkout release
```

The project initialization command asks several questions about your project:

```
project_name [Name of the project]: Apolo VSCode
project_dir [apolo-vscode]:
project_id [apolo-vscode]:
code_directory [modules]: 
preserve Neuro Flow template hints [yes]:
```

## Configuring the project

Add `debugpy` to your project's `requirements.txt` file (located in the project's root folder):

```bash
apolo-flow

flake8
mypy
isort
black
debugpy
```

Add the following lines to the beginning of your code file. In this example, it's `modules/train.py`.

```bash
import debugpy
debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()
```

Next, configure the project's environment on the platform:

```bash
$ apolo-flow build myimage
```

When the image is built, you can upload your code from a local file to the platform storage:

```
$ apolo-flow upload code
```

By default, this will upload everything from your project's `modules` folder to the `storage:<your_project_id>/modules` storage folder. To configure the source and the target for this command, go to your project's `.neuro/live.yml` file and find the `code` section under `volumes`:

```
volumes:
  data:
    remote: storage:$[[ flow.project_id ]]/data
    mount: /project/data
    local: data
  code:
    remote: storage:$[[ flow.project_id ]]/modules
    mount: /project/modules
    local: modules
  config:
    remote: storage:$[[ flow.project_id ]]/config
    mount: /project/config
    local: config
    read_only: True
```

Here, you can specify your local code folder and the storage folder you want to upload this code to.

## Running your code

In this example, we will be running a training job based on the code contained in the `train.py` file we just uploaded to the platform storage. To do this, run:

```
$ apolo-flow run train
```

Once the job is running, detach from it by pressing **Ctrl+P, Ctrl+Q** and run the following command:

```
$ apolo job port-forward <job-id> 5678:5678
```

This will allow you to access the job by the `5678` port.

## Debugging

Open your code file in VS Code and navigate to **Run > Start Debugging** or press **F5**:

![](<../../../../.gitbook/assets/image (89) (1).png>)

Select **Remote Attach**:

![](<../../../../.gitbook/assets/image (88).png>)

Enter **localhost** as the host name and the job's port number (in this case, it's **5687**):

![](<../../../../.gitbook/assets/image (87) (1).png>)

![](<../../../../.gitbook/assets/image (91).png>)

When this is done, you can set the breakpoint and start debugging.



---
File: /docs/apolo-console/apps/pre-installed/buckets.md
---

---
description: Apolo object storage
---

# Buckets

## Overview

The Buckets application in the Apolo Console provides a user interface for managing cloud storage buckets within a specific project and cluster. Buckets can be used to store and organize large amounts of data, such as backups, application data, and other persistent resources, across cloud providers.

This application is accessible from the left-side navigation menu in the Apolo Console. The buckets page displays all storage buckets associated with the selected project and cluster, provides details about each bucket, and offers the option to manage credentials.

![](../../../.gitbook/assets/console_screenshots/buckets.png)

## Bucket credentials

For each bucket you can create its own provider-specific credentials with the specific role _Read-Only_ or _Read & Write_. For AWS or MinIO providers those will be secret key ID and access key values, for GCP it will be a JSON key file, etc.&#x20;

The web console interface provides the ability to create several credentials with different roles and to review details for previously created.

![](../../../.gitbook/assets/console_screenshots/buckets_cred_det.png)

For other operations like uploading and downloading objects, bucket size, creating signed URLs for the objects, importing pre-existing buckets and many more, please refer to the Apolo CLI reference.

For data migration you could also refer Apolo Extras package usage. For extreme amounts of data, please reach us [support@apolo.us](mailto:support@apolo.us).

## References

* [Apolo CLI Buckets reference](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/blob)
* [Apolo Extras data operations](https://app.gitbook.com/s/EicNFI9vPOX1TTMYRKT9/#data-operations)



---
File: /docs/apolo-console/apps/pre-installed/disks.md
---

---
description: Apolo block storage
---

# Disks

## Overview

As opposed to standard platform storage, disks provide a faster, short-lived, non-partitioned space for jobs. This makes disks perfect for manipulating large amounts of data.

For example, if there's a large dataset that you need to process, it's better to create a disk, upload all of the required data from the storage to this disk, and only then perform all the necessary operations. In some cases, this can save you about 10%-20% of time depending on the amount of data and the operations you perform with it. After the data is processed, you can download it back to the storage for further use.

The Disks section is accessible via the left-hand navigation menu in the Apolo Console. It allows users to:

* Create new disks.
* View details of existing disks.
* Manage and delete disks.

## Creating a New Disk

1. Click "Create New Disk" button.
2. Fill out disk details:
   * _Storage:_ Specify the storage size in GB. This determines the disk's capacity.
   * _Name:_ Provide a unique name to identify the disk within the cluster.
   * _Lifespan:_ Define the disk’s lifespan using a duration format (e.g., 1d for one day, 2h for two hours, etc.). Lifespan determines how long the disk is allowed to exist without a use before it is automatically garbage-collected.
3. Click "Create" button.

## Viewing Disk Details

1. Select a disk from the grid to display its details in the right-hand panel.
2. Review the following information:
   * _ID:_ The unique identifier for the disk.
   * _Status:_ Indicates whether the disk is ready for use or still being processed.
   * _Owner:_ Displays the author of the disk.
   * _Storage:_ Total storage capacity of the disk.
   * _Lifespan:_ Defined time before the disk gets garbage-collected.
   * _Created:_ The date the disk was created.

Additionally, the properties pop-up includes two buttons: one for sharing access to the selected disk and another for removing the disk.

## References

* [Apolo CLI: Disk management](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/disk)
* [Apolo CLI: Disk usage](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/job#run)



---
File: /docs/apolo-console/apps/pre-installed/files.md
---

---
description: Apolo NFS storage
---

# Files

## Overview

The Files application is a comprehensive file management system designed to help you organize and manage your network storage within the cluster. This documentation will guide you through its features and functionality using Apolo Console. To learn more about how to manage the Files app with Apolo CLI, visit the [Apolo CLI Files](../../../apolo-concepts-cli/apps/files.md) app page.

## **Storage Organization**

Your organization receives a storage space within the cluster, structured in a hierarchical manner:

* Organization Level: The root folder for all your organization's files
* Project Level: Individual project folders within your organization
* Custom Folders: User-created folders for further organization

![](../../../.gitbook/assets/console_screenshots/FilesAppStructure.png)

## **Core Features**

_**Adding New Folders**_ You can create new folders to organize your files by clicking the "Add Folder" button. The system will prompt you with a dialog where you can specify the folder name. These folders help maintain a structured file hierarchy within your project space.

_**File Upload**_ The system supports file uploads through two methods:

1. Using the "Upload" button
2. Drag-and-drop functionality directly into the interface

_**Navigation and Search**_ The interface provides several navigation tools:

* Search bar: Located at the top of the interface for quick file location
* Home button: Returns you to your project's root folder
* Grid/List view toggle: Allows you to switch between viewing modes
* Folder Up: Navigate to the parent folder using the dedicated button

_**File and Folder Management**_

For each file and folder, you can:

* View properties including:
  * Save location (full path)
  * File extension
  * Last modified date
  * File size
* Perform actions such as:
  * Rename items
  * Delete items
  * Copy/move items
  * View detailed properties

## References

* [Apolo CLI Files management commands](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/storage)
* [Apolo CLI Files mounting to jobs](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/job#usage-10)
* [Apolo Flow configuration volumes definition](https://app.gitbook.com/s/-MMLOF_FqiWBMcOdY8cj/workflow-syntax/live-workflow-syntax#volumes)




---
File: /docs/apolo-console/apps/pre-installed/flows.md
---

---
description: Apolo pipelines
---

# Flows

**Apolo Flow** is a powerful pipeline engine designed for MLOps workflows on the Apolo platform. It enables seamless orchestration, automation, and execution of machine learning pipelines.

## Use Cases

* Automating ML workflows, from data ingestion to model deployment.
* Running batch and live workflows for continuous training and inference.
* Managing dependencies and execution order across pipeline steps.
* Standardizing and versioning workflows for reproducibility and collaboration.

## Example Use Case

Imagine a data science team working on a fraud detection model. They can use Apolo Flow to:

1. Ingest transaction data from multiple sources.
2. Preprocess the data and extract relevant features.
3. Train and validate multiple models in parallel.
4. Deploy the best-performing model into production.

## Models of Operation

* **CLI Usage**: Provides a command-line interface for managing pipelines, configuring workflows, and executing actions.
* **Configuration Files**: Uses structured configuration files to define workflow syntax, actions, and dependencies.
* **Workflow Syntax**: Supports batch (pipeline) and live (interactive) workflows, allowing users to define execution logic and contexts.

## Web Console Capabilities

Apolo Web console  includes a Flow section for monitoring and managing pipeline execution. Users can:

* List workloads running as part of flows, including live jobs and bakes (batch execution).
* Monitor and control the lifecycle of jobs, tasks, and entire pipelines.
* Retrieve pipeline statuses, view pipeline DAG with highlighted statuses, step-by-step execution details, inspect logs.
* Kill jobs, individual tasks, or full pipeline if necessary.
* Access detailed outputs for each pipeline step, enabling debugging and performance optimization.

For detailed documentation, refer to the dedicated Apolo Flow reference guide.

## References

* [Apolo Flow documentation](https://app.gitbook.com/o/-MMLX64i1AQdS3ehf2Kg/s/-MMLOF_FqiWBMcOdY8cj/)




---
File: /docs/apolo-console/apps/pre-installed/images.md
---

---
description: Apolo container image registry
---

# Images

## Overview

The Images app provides a central location for viewing properties of container image assets used in deployments.

The Images application is accessible from the left-side navigation menu in the Apolo Console. All container images associated with the selected project and cluster, along with detailed information about each image. Each image is represented by a path.

A search field at the top of the list allows you to quickly locate specific images by name or path.

On the right side of the screen, selecting an image displays detailed information about it, including:

* _Image Tags_. Tags associated with the image. Useful for version control (e.g., latest).
* _Image Path_. The full path to the image within the Apolo storage.
* _Creation Date_. The date when the image was added.
* _Size_. Total size of the image.
* _Copy Icons_. Allows the user to copy either the image path or tag to the clipboard for easy reference.

To learn more about managing images with the Images app, visit the [Apolo CLI Images](../../../apolo-concepts-cli/apps/images.md#overview) app page.

## References

* [Apolo CLI images reference](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/image)
* [Apolo Extras image build](https://app.gitbook.com/s/EicNFI9vPOX1TTMYRKT9/cli#apolo-extras-image)
* [Apolo Flow image configuration syntax](https://app.gitbook.com/s/-MMLOF_FqiWBMcOdY8cj/workflow-syntax/batch-workflow-syntax/batch-contexts#images-context)




---
File: /docs/apolo-console/apps/pre-installed/README.md
---

# Pre-installed apps

| App name              | Description                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [Files](files.md)     | A file manager facilitating access to the underlying network storage within the cluster.                                                     |
| [Buckets](buckets.md) | An object storage service that enables the creation of buckets, credential acquisition, and efficient management of stored objects.          |
| [Disks](disks.md)     | An app for managing block storage, streamlining the configuration, allocation, and maintenance of persistent disks.                          |
| [Images](images.md)   | A UI for the container image registry available within the cluster.                                                                          |
| [Secrets](secrets.md) | A secure secret store integrated with other apps, ensuring safe management and usage of credentials and keys.                                |
| [Jobs](jobs/)         | A tool enabling the execution of containerized workloads, seamlessly integrated with other apps and cluster resources.                       |
| [Flows](flows.md)     | A workflow engine designed to execute jobs organized in Directed Acyclic Graphs (DAGs) with integrated data caching for enhanced efficiency. |



---
File: /docs/apolo-console/apps/pre-installed/secrets.md
---

---
description: Apolo secrets management
---

# Secrets

## Overview

The Secrets app in the Apolo Console allows users to securely store and manage sensitive data, such as API tokens, passwords, configuration values or files associated with their projects.

Secrets ensure that sensitive information remains protected while being accessible only to workloads of an authorized users within your project.

The Secrets app, accessible from the left-hand navigation menu, provides a centralized interface to:

* Create and manage secure key-value pairs.
* View a list of existing secrets in your project.
* Delete secrets that are no longer required.

{% hint style="info" %}
Once the secret is created, you can not read it's value via Apolo Console, Apolo CLI or update it.

You can only delete the existing secret and create a new one.

When you remove the secret, the currently running workloads will stay intact even if you recreate the secret.
{% endhint %}

To learn more about secrets management via Apolo CLI visit a [dedicated documentation](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/secret) page.

If you are interested in secrets usage with Apolo Jobs, please check [this](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/topics/topic-secrets) page.

The use of secrets in Flows is the same as in the CLI. Simply reference your secret name in environment variable value or in volume mount configuration sections of tasks or volumes. For more details, check our [Flow documentation](https://app.gitbook.com/s/-MMLOF_FqiWBMcOdY8cj/workflow-syntax/live-workflow-syntax).&#x20;

## References

* [Apolo CLI: Secrets management](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/commands/secret)
* [Apolo CLI: Secrets usage](https://app.gitbook.com/s/-MOkWy7dB5MDbkSII8iF/topics/topic-secrets)
* [Apolo Flow: configuration file reference](https://app.gitbook.com/s/-MMLOF_FqiWBMcOdY8cj/workflow-syntax)




---
File: /docs/apolo-console/apps/README.md
---

# Apps

The Apolo console offers two categories of applications: [Pre-installed Apps](pre-installed/) and [Available Apps](available-apps/).

#### Pre-installed Apps

Pre-installed apps are essential tools that come standard with the Apolo console, giving ML engineers instant access to key functionalities and facilitating efficient processes without requiring any additional setup.

#### Available Apps

Available apps are a collection of popular and widely-used tools in the machine learning industry. These apps are not installed by default and must be installed before you can use them. You can explore and install any of these apps according to your project requirements.



---
File: /docs/apolo-console/getting-started/clusters.md
---

# Clusters

Clusters are collections of resources - compute, storage, and the registry. When you sign-up on Apolo, you could ask someone that have respective access level to add you to their organization. This provides access to clusters the organization has access to.

Under the hood, cluster is a [Kubernetes](https://kubernetes.io/) cluster being managed by Apolo services.

You can also create new clusters, but this requires additional access. For more information, contact [support@apolo.us](mailto:support@apolo.us).

You can use one cluster at a time and switch between clusters. This tutorial will helps you understand how you can manage resources.

### **How can I manage my clusters?**

Each cluster comes with its own storage, registry, resource presets and other services.

You can view information about your current cluster both in the CLI and in the Apolo Console:

{% tabs %}
{% tab title="CLI" %}
You can use the `apolo config show` command to view the current cluster's name, API URL, docker registry URL, and the list of presets available for this cluster.

```
$ apolo config show
User Configuration:                                       
 User Name            john-doe                      
 Current Cluster      default                             
 Current Org          <no-org>                            
 Current Project      myproject 
 Credits Quota        unlimited                           
 Jobs Quota           unlimited                           
 API URL              https://staging.neu.ro/api/v1       
 Docker Registry URL  https://registry.default.org.neu.ro 
Resource Presets:                                                                                                          
 Name               #CPU   Memory   Round Robin   Preemptible Node   GPU                     Jobs Avail   Credits per hour 

 cpu-small             1     4.0G                                                                  55   1                
 cpu-medium            3    11.0G                                                                  15   2                
 cpu-large             7    28.0G                                                                   7   4                
 gpu-k80-small         3    57.0G                                  1 x nvidia-tesla-k80            30   10               
 gpu-k80-small-p       3    57.0G                                  1 x nvidia-tesla-k80            10   1                
 gpu-v100-small        7    57.0G                                  1 x nvidia-tesla-v100           10   32               
 gpu-v100-small-p      7    57.0G                                  1 x nvidia-tesla-v100           10   4                
 gpu-small             3    57.0G                                  1 x nvidia-tesla-k80            30   10               
 gpu-small-p           3    57.0G                                  1 x nvidia-tesla-k80            10   1                
 gpu-v100-large       63   480.0G                                  8 x nvidia-tesla-v100            4   256              
 gpu-v100-large-p     63   480.0G                                  8 x nvidia-tesla-v100            4   32               
 gpu-v100-2           15   115.0M                                  2 x nvidia-tesla-v100           16   64               
 gpu-v100-4           31   235.0M                                  4 x nvidia-tesla-v100            8   128              
 gpu-v100-8           63   480.0M                                  8 x nvidia-tesla-v100            4   256
```
{% endtab %}

{% tab title="Apolo Console" %}
To view information about your current cluster in the Apolo Console, look at the top right corner of the screen. You will see a section labeled "Cluster" with the name of your current cluster (e.g., "default"). Clicking on the dropdown arrow next to the cluster name will provide more details about the current cluster.

![](/docs/.gitbook/assets/console_screenshots/cluster_inform.png)
{% endtab %}
{% endtabs %}

### **How can I view all my clusters and switch my current cluster?**

You can view the list of available clusters and switch between them both in the CLI and in the Apolo Console:

{% tabs %}
{% tab title="CLI" %}
You can use the `apolo config get-clusters` command to view the list of clusters that you have access to and information about them.

```
$ apolo config get-clusters
Fetch the list of available clusters...
Available clusters:
* Name: neuro-public
  Presets:
    Name         #CPU  Memory  Preemptible  GPU
    cpu-small       1    2.0G       No
    cpu-large       7   28.0G       No
    gpu-small       3   57.0G       No      1 x nvidia-tesla-k80
    gpu-small-p     3   57.0G      Yes      1 x nvidia-tesla-k80
    gpu-large       7   57.0G       No      1 x nvidia-tesla-v100
    gpu-large-p     7   57.0G      Yes      1 x nvidia-tesla-v100
  Name: onprem
  Presets:
    Name       #CPU  Memory  Preemptible  GPU                          
    cpu-small     1    4.0G       No                                   
    cpu-large     4   10.0G       No                                   
    gpu-small    23   60.0G       No      1 x nvidia-geforce-rtx-2080ti
    gpu-large    46  120.0G       No      2 x nvidia-geforce-rtx-2080ti
```

You can switch between clusters by using the `apolo config switch-cluster` command. When you run the command, you are prompted to enter the name of the cluster you want to switch to. The current cluster is switched after you provide the name.

```
$ apolo config switch-cluster
Fetch the list of available clusters...
Available clusters:
* Name: default
  Resource Presets:
   Name               #CPU   Memory   Preemptible   Preemptible Node   GPU
  ───────────────────────────────────────────────────────────────────────────────────────────
   cpu-small             1     4.0G        ×               ×
   cpu-medium            3    11.0G        ×               ×
   cpu-large             7    26.0G        ×               ×
   gpu-k80-small         5    48.0G        ×               ×           1 x nvidia-tesla-k80
   gpu-k80-small-p     5.0    48.0G        √               √           1 x nvidia-tesla-k80
   gpu-v100-small        5    95.0G        ×               ×           1 x nvidia-tesla-v100
   gpu-v100-small-p    5.0    95.0G        √               √           1 x nvidia-tesla-v100
  Name: onprem-poc
  Resource Presets:
   Name         #CPU   Memory   Preemptible   Preemptible Node   GPU
  ─────────────────────────────────────────────────────────────────────────────────────────────
   cpu-nano      0.2     1.0G        ×               ×
   cpu-small       1     4.0G        ×               ×
   cpu-large       4    10.0G        ×               ×
   gpu-small      23    60.0G        ×               ×           1 x nvidia-geforce-rtx-2080ti
   gpu-large      47   120.0G        ×               ×           2 x nvidia-geforce-rtx-2080ti
   gpu-1x3090   23.0    60.0G        ×               ×           1 x nvidia-geforce-rtx-3090
   gpu-2x3090   47.0   120.0G        ×               ×           2 x nvidia-geforce-rtx-3090
Select cluster to switch [default]: onprem-poc
The current cluster is onprem-poc
```
{% endtab %}

{% tab title="Apolo Console" %}
To view all your clusters and switch the current one, click on the dropdown arrow next to the cluster name in the top right corner. A menu will appear with all available clusters. Select the desired one to switch.

![](/docs/.gitbook/assets/console_screenshots/several_clusters.png)
{% endtab %}
{% endtabs %}

### **How can I view my credits?**

Usually, you are assigned a computation quota in term of credits. Those credits are consumed whenever you run a job. Credits are cluster-bound which means, you have different balances in different clusters.

You can view the remaining credits on your Apolo Console dashboard. The `apolo config show` command also shows the amount of credits left as part of its output too.

### How can I request for more credits?

You can top up your credits by clicking the **Credits** menu on the Apolo Console dashboard.

You can also contact [support@apolo.us](mailto:support@apolo.us) or corresponding cluster provider to learn about latest discounts and promotions, and then request the top up.

### How can I create a new cluster?

Apolo lets you create new clusters for better management and orchestration of resources. Before you create a cluster, you must decide on the presets, storage, and registry that you want to assign for this cluster. You can create a cluster by writing to us at [support@apolo.us](mailto:support@apolo.us).



---
File: /docs/apolo-console/getting-started/organizations.md
---

# Organizations

## Start with organization

Organizations are formed as a collections of users that have common access to some subset of clusters and could share credits.

After account creating you have two options:

* create your own organization;
* send your user name for adding to the existed organization.

![](/docs/.gitbook/assets/console_screenshots/choose_org.png)

By inviting other users into organizations, those users automatically obtain access to all clusters organization was added to.

When users run their apps within organization, they consume this organization credits which enables teams to have shared balance.

Team members could also top-up organization balance in Apolo web app by clicking on the Credits menu.

![](/docs/.gitbook/assets/console_screenshots/organizations_balance.png)

Refer to `apolo admin` for organizations administration and to `apolo config switch-org` to switch between organizations within your CLI config.

Most of Apolo CLI accept `--org` flag to perform various commands in corresponding organizations.

## Set up organization

As administrator you can set up your current organization or create one more lately.

![](/docs/.gitbook/assets/console_screenshots/organizations_1.png)

You can manage a user list and look through reports in organization settings.

![](/docs/.gitbook/assets/console_screenshots/org_settings.png)

Users tab contains the next functionality:

* inviting users to the organization;

![](/docs/.gitbook/assets/console_screenshots/org_set_invite_user.png)

* setting up user role;

![](/docs/.gitbook/assets/console_screenshots/org_set_edit_user.png)

* deleting user from organization.

![](/docs/.gitbook/assets/console_screenshots/org_set_remove_user.png)

Reports tab contains grafana dashboards.

## Organization roles

Organization participants could be of one of available roles: user, manager, admin. Each subsequent role expands on the previous one.

#### User

Only able to read organization participants, create own projects or being invited to other people's projects.

#### Manager

See all projects within the organization, configure user job's quotas, see organization artifacts, promote other users up to manager within the organization

#### Admin

Remove organization, promote other users up to admin within the organization.

When you create organization, you become it's administrator.



---
File: /docs/apolo-console/getting-started/projects.md
---

# Projects

Projects are units of collaboration on a platform.

Each Apolo platform artifact e.g. job, storage file, image, app instance, etc. belongs to some project.

Users could invite other users into their project specifying access level (reader / writer / manager / admin).

Refer to `apolo admin` for project administration and to `apolo config switch-project` to, well, switch between projects.

Most of Apolo CLI accept `--project` flag to perform various commands in corresponding projects.

### Project roles

Project contributors could have one of available roles: reader, writer, manager or admin. Each subsequent role expands on the previous one.

#### Reader

Readers are only able to read project artifacts: download / read storage, blobs, check job statuses and logs, access workloads via HTTP endpoints, pull images, etc.

#### Writer

User with this role is able to perform updates of artifacts -- write new files or update existing in storage or blobs, run new workloads or terminate existing, push images, etc.

#### Manager

Project managers could also invite other users into projects, promote/demote their roles up to manager access level.

#### Admin

Administrators are able to remove project, promote/demote administrators.

When you create project, you become it's administrator.



---
File: /docs/apolo-console/getting-started/README.md
---

# Getting started




---
File: /docs/apolo-console/getting-started/sign-up-login.md
---

# Sign Up, Login

### Sign-up

First of all you should create an account in [Apolo Console](https://console.apolo.us):

1. Go to [Apolo Console](https://console.apolo.us);

![](/docs/.gitbook/assets/console_screenshots/Sign-up.png)

1. Click "Sign-up" button;
2. Enter your e-mail and create a password;
3. Click "Continue" button;
4. Verify your e-mail via verification link which was sent to your e-mail;
5. Enter your username and click "Sign up" button;
6. Read and accept terms of use agreement;
7. Start your onboarding from [connecting or creating organization](organizations.md).

Also, you can create your account using Google or GitHub accounts.

### Login

On the login page you can execute login using your credentials. On this page you have availability to reset your password in case you forgot it.

![](/docs/.gitbook/assets/console_screenshots/login.png)

### Forgot password

In case of forgetting your password, follow this instruction:

1. Click "Forgot password" button;

![](/docs/.gitbook/assets/console_screenshots/forgot-pass.png)

2. Enter your email;
3. Follow the instructions which was sent to your e-mail.

![](/docs/.gitbook/assets/console_screenshots/forgot-pass_1.png)



---
File: /docs/getting-started/first-steps/getting-started.md
---

# Getting Started

## Introduction

There are two things you will need to do before you start working with Apolo:

1. [Install the CLI client](../../apolo-concepts-cli/installing.md).
2. [Understand the platform's main concepts](getting-started.md#understanding-the-main-concepts).

After this, you're free to explore the platform and it's functionality. As a good starting point, we've included a section about [development on GPU with Jupyter Notebooks](getting-started.md#developing-on-gpu-with-jupyter-notebooks).

## Understanding the main concepts

On the **Apolo** level, you will work with jobs, environments, and storage. To be more specific, a job (an execution unit) runs in a given environment (Docker container) on a given preset (a combination of CPU, GPU, and memory resources allocated for this job) with several storage instances (block or object storage) attached.

Here are some examples.

### Hello, World!

Run a job on CPU which prints “Hello, World!” and shuts down:

```bash
apolo run --preset cpu-small --name test ubuntu -- echo Hello, World!
```

Executing this command will result in an output like this:

```
√ Job ID: job-7dd12c3c-ae8d-4492-bdb9-99509fda4f8c
√ Name: test
- Status: pending Creating
- Status: pending Scheduling
- Status: pending ContainerCreating
√ Http URL: https://test--jane-doe.jobs.default.org.neu.ro
√ The job will die in a day. See --life-span option documentation for details.
√ Status: succeeded
√ =========== Job is running in terminal mode ===========
√ (If you don't see a command prompt, try pressing enter)
√ (Use Ctrl-P Ctrl-Q key sequence to detach from the job)
Hello, World!
```

### A simple GPU job

Run a job on GPU in the default Apolo environment (`ghcr.io/neuro-inc/base`) that checks if CUDA is available in this environment:

```
apolo run --preset gpu-small --name test  ghcr.io/neuro-inc/base -- python -c "import torch; print(torch.cuda.is_available());"
```

We used the `gpu-small` preset for this job. To see the full list of presets you can use, run the following command:

```
apolo config show
```

### Working with platform storage

Create a new `demo` directory in the root directory of your platform storage:

```
apolo mkdir -p storage:demo
```

Run a job that mounts the `demo` directory from platform storage to the `/demo` directory in the job container and creates a file in it:

```
apolo run --volume storage:demo:/demo:rw ubuntu -- bash -c "echo Hello >> /demo/hello.txt"
```

Check that the file you have just created is actually on the storage:

```
apolo ls storage:demo
```

## Developing on GPU with Jupyter Notebooks

Development in Jupyter Notebooks is a good example of how the Apolo Platform can be used. While you can run a Jupyter Notebooks session in one command through CLI or in one click in the Console, we recommend project-based development. To simplify the process, we provide a project template which is based on the [**cookiecutter** package](https://github.com/cookiecutter/cookiecutter). This template provides the basic necessary folder structure and integrations with several recommended tools.

### Initializing a Apolo cookiecutter flow

First, you will need to install the **cookiecutter** package via **pip** or **pipx**:

```
pipx install cookiecutter
```

Now, to initialize a new Apolo flow using [cookiecutter](https://github.com/neuro-inc/cookiecutter-neuro-project/blob/master/cookiecutter.json) template, run:

```
cookiecutter gh:neuro-inc/cookiecutter-neuro-project --checkout release
```

This command will prompt you to enter some info about your new flow:

```
project_name [Neuro Project]: New Cookiecutter Project
project_dir [new cookiecutter project]:
project_id [new_cookiecutter_project]:
code_directory [modules]:
preserve Neuro Flow template hints [yes]:
```

{% hint style="info" %}
Default values are indicated by square brackets **\[ ].** You can use them by pressing **Enter**.
{% endhint %}

To navigate to the flow directory, run:

```
cd new-cookiecutter-project
```

### Flow structure

The structure of the project's folder will look like this:

```
new-cookiecutter-project
├── .github/            <- Github workflows and a dependabot.yml file
├── .neuro/             <- apolo and apolo-flow CLI configuration files
├── config/             <- configuration files for various integrations
├── data/               <- training and testing datasets (we don't keep it under source control)
├── notebooks/          <- Jupyter notebooks
├── modules/            <- models' source code
├── results/            <- training artifacts
├── .gitignore          <- default .gitignore file for a Python ML project
├── .neuro.toml         <- autogenerated config file for Apolo CLI
├── .neuroignore        <- a file telling Apolo CLI which files to ignore while uploading to the platform storage
├── HELP.md             <- autogenerated template reference
├── README.md           <- autogenerated informational file
├── Dockerfile          <- description of the docker image used for training in your flow
├── apt.txt             <- list of system packages to be installed in the training environment
├── requirements.txt    <- list of Python dependencies to be installed in the training environment
├── setup.cfg           <- linter settings (Python code quality checking)
└── update_actions.py   <- script used to update apolo-flow actions in one of the GitHub workflows
```

The template contains the `.neuro/live.yaml` configuration file for `apolo-flow`. This file guarantees a proper connection between the flow structure, the base environment that we provide, and actions with storage and jobs. For example, the `upload` command synchronizes sub-folders on your local machine with sub-folders on the persistent platform storage, and those sub-folders are synchronized with the corresponding sub-folders in job containers.

### Setting up the environment and running Jupyter

To set up the project environment, run:

```
apolo-flow build train
apolo-flow mkvolumes
```

When these commands are executed, system packages from `apt.txt` and pip dependencies from `requirements.txt` are installed to the base environment. It supports CUDA by default and contains the most popular ML/AI frameworks such as Tensorflow and Pytorch.

For Jupyter Notebooks to run properly, the `train.py` script and the notebook itself should be available on the storage. Upload the `code` directory containing this file to the storage by using the following command:

```
apolo-flow upload ALL
```

Now you need to choose a preset on which you want to run your Jupyter jobs. To view the list of presets available on the current cluster, run:

```
apolo config show 
```

To start a Jupyter Notebooks session run:

```
apolo-flow run jupyter
```

This command will open Jupyter Notebooks interface in your default browser.

{% hint style="info" %}
Also, you can adjust the _jupyter_ job's preset configuration by specifying the _**preset**_ argument to reflect your preferred preset:

```
jupyter:
    action: gh:neuro-actions/jupyter@<version>
    args:
      ...
      preset: <gpu-preset-name>
      ...
```

After this, each time you run a Jupyter job, it will use the specified by default without the need for you to provide it in a CLI command:

```
$ apolo-flow run jupyter 
```

[You can find more information about job description arguments here](https://github.com/neuro-actions/jupyter#arguments)
{% endhint %}

Now, when you edit notebooks, they are updated on your platform storage. To download them locally (for example, to save them under a version control system), run:

```
apolo-flow download notebooks
```

Don’t forget to terminate your job when you no longer need it (the files won’t disappear after that):

```
apolo-flow kill jupyter
```

To check how many credits you have left, run:

```
apolo config show
```



---
File: /docs/getting-started/first-steps/README.md
---

# First Steps

This group contains the following topics:

{% content-ref url="getting-started.md" %}
[getting-started.md](getting-started.md)
{% endcontent-ref %}

{% content-ref url="training-your-first-model.md" %}
[training-your-first-model.md](training-your-first-model.md)
{% endcontent-ref %}

{% content-ref url="running-your-code.md" %}
[running-your-code.md](running-your-code.md)
{% endcontent-ref %}

{% content-ref url="collaborative-development.md" %}
[collaborative-development.md](collaborative-development.md)
{% endcontent-ref %}




---
File: /docs/getting-started/first-steps/running-your-code.md
---

# Running Your Code

Oftentimes you don't start a project from scratch. Instead of that you use someone's or your own old code as a baseline and develop your solution on top of it. This guide demonstrates how to take an existing code base, convert it into a Apolo flow, and start developing on the platform.

## Prerequisites

1. Make sure that you have the Apolo CLI [installed](getting-started.md#installing-cli) and logged in.
2. Install the `apolo-flow` package:

```bash
pip install -U apolo-flow
```

## Configuration

As an example we'll use the GitHub [repo](https://github.com/songyouwei/ABSA-PyTorch) that contains PyTorch implementations for Aspect-Based Sentiment Analysis models (see [Attentional Encoder Network for Targeted Sentiment Classification](https://paperswithcode.com/paper/attentional-encoder-network-for-targeted) for more details).

First, let's clone the repo and navigate to the created folder:

```bash
git clone git@github.com:songyouwei/ABSA-PyTorch.git
cd ABSA-PyTorch
```

Now, we need to create two more files in this folder:

* `Dockerfile` contains a very basic Docker image configuration. We need this file to build a custom Docker image which is based on `pytorch/pytorch` public images and contains this repo requirements (which are gracefully listed by the repo maintainer in `requirements.txt`):

{% code title="Dockerfile" %}
```bash
FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime
COPY . /cfg
RUN pip install --progress-bar=off -U --no-cache-dir -r /cfg/requirements.txt
```
{% endcode %}

* `.neuro/live.yml` contains minimal configuration allowing us to run this repo's scripts right on the platform through handy short commands:

{% code title=".neuro/live.yml" %}
```yaml
kind: live
title: Sentiment Analysis Training
id: absa

volumes:
  project:
    remote: storage:${{ flow.id }}
    mount: /project
    local: .

images:
  pytorch:
    ref: image:${{ flow.id }}:v1.0
    dockerfile: ${{ flow.workspace }}/Dockerfile
    context: ${{ flow.workspace }}

jobs:
  train:
    image: ${{ images.pytorch.ref }}
    preset: gpu-small
    name: absa-pytorch-train
    volumes:
      - ${{ volumes.project.ref_rw }}
    bash: |
        cd ${{ volumes.project.mount }}
        python train.py --model_name bert_spc --dataset restaurant
```
{% endcode %}

Here is a brief explanation of this config:

* `volumes` section contains declarations of connections between your computer file system and the platform storage; here we state that we want the entire project folder to be uploaded to storage at `storage:absa` folder and be mounted inside jobs `/project`;
* `images` section contains declarations of Docker images created in this project; here we declare our image which is decribed in `Dockerfile` above;
* `jobs` section is the one where action happens; here we declare a `train` job which runs our training script with a couple of parameters.

## Running code

Now it's time to run several commands that set up the project environment and run training.

* First, create volumes and upload project to platform storage:

```
apolo-flow mkvolumes
apolo-flow upload ALL
```

* Then, build an image:

```
apolo-flow build pytorch
```

* Finally, run training:

```
apolo-flow run train
```

Please run `apolo-flow --help` to get more information about available commands.



---
File: /docs/getting-started/first-steps/training-your-first-model.md
---

# Training Your First Model

## Introduction

In this tutorial, we describe the recommended way to train a simple machine learning model on the Apolo platform. As our ML engineers prefer PyTorch over other ML frameworks, we show the training and evaluation of one of the basic PyTorch examples.

We assume that you have already signed up to the platform, installed the Apolo CLI, and logged in to the platform (see [Getting Started](getting-started.md)).

We base our example on the [Classifying Names with a Character-Level RNN](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html) tutorial.

## Initializing a new flow

To simplify working with Apolo Platform and to help establish the best practices in the ML environment, we provide a [flow template](https://github.com/neuro-inc/flow-template). This template consists of the recommended directories and files. It's designed to operate smoothly with our [base environment.](../apolo-base-docker-image.md)

To use it, install the [**cookiecutter**](https://github.com/cookiecutter/cookiecutter) package and initialize **cookiecutter-neuro-project**:

```
pipx install cookiecutter
cookiecutter gh:neuro-inc/cookiecutter-neuro-project --checkout release
```

You will then need to provide some information about the new project:

```
project_name [Name of the project]: Apolo Tutorial
project_dir [neuro-tutorial]:
project_id [neuro-tutorial]:
code_directory [modules]: rnn
preserve Neuro Flow template hints [yes]:
```

## Flow configuration structure

After you execute the command mentioned above, you get the following structure:

```
apolo-tutorial
├── .github/            <- Github workflows and a dependabot.yml file
├── .neuro/             <- apolo and apolo-flow CLI configuration files
├── config/             <- configuration files for various integrations
├── data/               <- training and testing datasets (we don't keep it under source control)
├── notebooks/          <- Jupyter notebooks
├── rnn/                <- models' source code
├── results/            <- training artifacts
├── .gitignore          <- default .gitignore file for a Python ML project
├── .neuro.toml         <- autogenerated config file
├── .neuroignore        <- a file telling apolo to ignore the results/ folder
├── HELP.md             <- autogenerated template reference
├── README.md           <- autogenerated informational file
├── Dockerfile          <- description of the base image used for your project
├── apt.txt             <- list of system packages to be installed in the training environment
├── requirements.txt    <- list of Python dependencies to be installed in the training environment
├── setup.cfg           <- linter settings (Python code quality checking)
└── update_actions.py   <- instructions on update actions
```

When you run a job (for example, via `apolo-flow run jupyter`), the directories are mounted to the job as follows:

| Mount Point           | Description              | Storage URI                         |
| --------------------- | ------------------------ | ----------------------------------- |
| `/project/data/`      | Training / testing data  | `storage:neuro-tutorial/data/`      |
| `/project/rnn/`       | User's Python code       | `storage:neuro-tutorial/rnn/`       |
| `/project/notebooks/` | User's Jupyter notebooks | `storage:neuro-tutorial/notebooks/` |
| `/project/results/`   | Logs and results         | `storage:neuro-tutorial/results/`   |

## Filling the flow

Now we need to fill newly created flow with the content:

* Change working directory:

```
cd apolo-tutorial
```

* Copy the [model source](https://github.com/pytorch/tutorials/blob/master/intermediate_source/char_rnn_classification_tutorial.py) to your `rnn` folder:

```
curl https://raw.githubusercontent.com/pytorch/tutorials/master/intermediate_source/char_rnn_classification_tutorial.py -o rnn/char_rnn_classification_tutorial.py
```

* Download data from [here](https://download.pytorch.org/tutorial/data.zip), extract the ZIP’s content and put it in your `data` folder:

```
curl https://download.pytorch.org/tutorial/data.zip -o data/data.zip && unzip data/data.zip && rm data/data.zip
```

## Training and evaluating the model

When you start working with a flow on the Apolo platform, the basic flow looks as follows: you set up the remote environment, upload data and code to your storage, run training, and evaluate the results.

To set up the remote environment, run

```
apolo-flow build train
```

This command will run a lightweight job (via `apolo run`), upload the files containing your dependencies `apt.txt` and `requirements.txt` (via `apolo cp`), install the dependencies (using `apolo exec`), do other preparatory steps, and then create the base image from this job and push it to the platform (via `apolo save`, which works similarly to `docker commit`).

To upload data and code to your storage, run

```
apolo-flow upload ALL
```

To run training job, you need to specify the training script in `.neuro/live.yaml`, and then run `apolo-flow run train`:

* open `.neuro/live.yaml` in an editor,
* find the following lines (make sure you're looking at the `train` job, not `multitrain` which has a very similar section):

```
    bash: |
        cd $[[ volumes.project.mount ]]
        python -u $[[ volumes.code.mount ]]/train.py --data $[[ volumes.data.mount ]]
```

* and replace it with the following lines:

```
    bash: |
        cd $[[ volumes.project.mount ]]
        python -u $[[ volumes.code.mount ]]/char_rnn_classification_tutorial.py
```

Now, you can run

```
apolo-flow run train
```

and observe the output. You will see how some checks are made at the beginning of the script, and then the model is being trained and evaluated:

```
['data/names/German.txt', 'data/names/Polish.txt', 'data/names/Irish.txt', 'data/names/Vietnamese.txt', 
'data/names/French.txt', 'data/names/Japanese.txt', 'data/names/Spanish.txt', 'data/names/Chinese.txt', 
'data/names/Korean.txt', 'data/names/Czech.txt', 'data/names/Arabic.txt', 'data/names/Portuguese.txt', 
'data/names/English.txt', 'data/names/Italian.txt', 'data/names/Russian.txt', 'data/names/Dutch.txt', 
'data/names/Scottish.txt', 'data/names/Greek.txt']
Slusarski
['Abandonato', 'Abatangelo', 'Abatantuono', 'Abate', 'Abategiovanni']
tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0.]])
torch.Size([5, 1, 57])
tensor([[-2.8248, -2.9118, -2.8999, -2.9170, -2.8916, -2.9699, -2.8785, -2.9273,
         -2.8397, -2.8539, -2.8764, -2.9278, -2.8638, -2.9310, -2.9546, -2.9008,
         -2.8295, -2.8441]], grad_fn=<LogSoftmaxBackward>)
('German', 0)
category = Vietnamese / line = Vu
category = Chinese / line = Che
category = Scottish / line = Fraser
category = Arabic / line = Abadi
category = Russian / line = Adabash
category = Vietnamese / line = Cao
category = Greek / line = Horiatis
category = Portuguese / line = Pinho
category = Vietnamese / line = To
category = Scottish / line = Mcintosh
5000 5% (0m 19s) 2.7360 Ho / Portuguese ✗ (Vietnamese)
10000 10% (0m 38s) 2.0606 Anderson / Russian ✗ (Scottish)
15000 15% (0m 58s) 3.5110 Marqueringh / Russian ✗ (Dutch)
20000 20% (1m 17s) 3.6223 Talambum / Arabic ✗ (Russian)
25000 25% (1m 35s) 2.9651 Jollenbeck / Dutch ✗ (German)
30000 30% (1m 54s) 0.9014 Finnegan / Irish ✓
35000 35% (2m 13s) 0.8603 Taverna / Italian ✓
40000 40% (2m 32s) 0.1065 Vysokosov / Russian ✓
45000 45% (2m 52s) 3.6136 Blanxart / French ✗ (Spanish)
50000 50% (3m 11s) 0.0969 Bellincioni / Italian ✓
55000 55% (3m 30s) 3.1383 Roosa / Spanish ✗ (Dutch)
60000 60% (3m 49s) 0.6585 O'Kane / Irish ✓
65000 65% (4m 8s) 4.7300 Satorie / French ✗ (Czech)
70000 70% (4m 27s) 0.9765 Mueller / German ✓
75000 75% (4m 46s) 0.7882 Attia / Arabic ✓
80000 80% (5m 5s) 2.1131 Till / Irish ✗ (Czech)
85000 85% (5m 25s) 0.5304 Wei / Chinese ✓
90000 90% (5m 44s) 1.6258 Newman / Polish ✗ (English)
95000 95% (6m 2s) 3.2015 Eberhardt / Irish ✗ (German)
100000 100% (6m 21s) 0.2639 Vamvakidis / Greek ✓

> Dovesky
(-0.77) Czech
(-1.11) Russian
(-2.03) English

> Jackson
(-0.92) English
(-1.65) Czech
(-1.85) Scottish

> Satoshi
(-1.32) Italian
(-1.81) Arabic
(-2.14) Japanese
```



---
File: /docs/getting-started/apolo-base-docker-image.md
---

# Apolo Base Docker image

Our company provides a public Docker image with pre-configured **Conda environments** and pre-installed **Python dependencies**, designed to simplify development and deployment. This image ensures compatibility, consistency, and efficiency across diverse workflows, making it an ideal solution for streamlined integration into your projects.

Explore the guide below for setup instructions and configuration details.

## Github repo

The **GitHub repository** serves as the primary source of truth for all updates, configurations, and detailed documentation regarding this Docker image.

[https://github.com/neuro-inc/neuro-base-environment](https://github.com/neuro-inc/neuro-base-environment)

### Releases

Releases can be found in [Releases github tab](https://github.com/neuro-inc/neuro-base-environment/releases)

Each release includes four Docker images, each configured with a specific set of dependencies.

Dependencies version can be found in the specific release page. [Example](https://github.com/neuro-inc/neuro-base-environment/releases/tag/v24.12.0)

## Usage

You can utilize our docker image in various ways, pulling it from public repository, using it locally or in Apolo jobs.

**Base path**

```
ghcr.io/neuro-inc/base
```

**Non-versioned tags**

```
latest-runtime-minimal
latest
latest-runtime
latest-devel
latest-devel-minimal
```

**Apolo-flow**

when you are creating Apolo flow using our template, by default we expose base Docker

{% embed url="https://github.com/neuro-inc/flow-template" %}
Apolo flow repo
{% endembed %}

{% embed url="https://github.com/neuro-inc/flow-template-barebone" %}
Apolo flow barebone
{% endembed %}

Also, if you don't want to edit the Dockerfile, you can specify docker directly in your job .neuro/live.yml

```
......... .neuro/live.yml

kind: live
title: My flow
defaults:
   .......
jobs:
  job:
    args:
      image: ghcr.io/neuro-inc/base:latest
```

## Conda environments

By default, our Docker image provides three Conda environments:

*   **Default**: Automatically activated through the `.bashrc` configuration for all terminal sessions

    can be activated using

    <pre><code><strong>conda activate base 
    </strong>OR
    <strong>source /opt/conda/bin/activate base
    </strong></code></pre>
*   **TensorFlow-specific**: Optimized for TensorFlow workflows.\
    can be activated using

    <pre><code><strong>conda activate tf 
    </strong>OR
    <strong>source /opt/conda/bin/activate tf
    </strong></code></pre>
*   **Torch-specific**: Tailored for PyTorch operations.

    can be activated using

    <pre><code><strong>conda activate torch 
    </strong>OR
    <strong>source /opt/conda/bin/activate torch
    </strong></code></pre>

**Environment**

We strive to keep dependencies up-to-date. If you require a more recent version or believe an update could enhance the platform, please reach out to us. Alternatively, you can extend our base Dockerfile to install any additional dependencies you need.

```
FROM ghcr.io/neuro-inc/base:v24.12.0-runtime
RUN pip install ...
```

## References

* [Base Docker repository](https://github.com/neuro-inc/neuro-base-environment/tree/master)
* [Base Apolo flow template using the latest Docker](https://github.com/neuro-inc/flow-template)



---
File: /docs/getting-started/faq.md
---

# FAQ

### How to Upload and Download Data

You can upload your datasets to the Platform using Neuro CLI. Neuro CLI supports basic file system operations for copying and moving files to and from the platform storage.

From your terminal or command prompt, change to the directory containing your dataset, and run:

```
neuro cp -r data/ storage:data/
```

The URI `storage:data/` indicates that the destination is the platform. In a similar fashion,

```
neuro cp -r storage:data/ data/
```

downloads dataset to your current directory locally.

You can access your dataset from within a container by giving `--volume storage:data/:/var/storage/data/:rw` to `neuro run` as a parameter when starting a new job.

If your aim is to download or upload data from external system, be it AWS S3 bucket, or Azure Blob Storage, checkout our [extras](https://app.gitbook.com/s/EicNFI9vPOX1TTMYRKT9/#data-operations) package usage.

### How to Connect to a Running Job

To work with your dataset from within a container, to troubleshoot a model, or to get shell access to a GPU instance, you can execute a command shell within a running job in interactive mode.

To do so, copy the job id of a running job (you can run `neuro ps` to see the list), and run:

```
neuro exec <job-id or job-name> bash
```

For example,

```
neuro exec training bash
```

This command starts bash within the running job and connects your terminal to it.

### How to Run a Job in a Custom Environment

Assuming you have a local Docker image named `helloworld` built on your local machine, you can push it to the Neuro Platform by running:

```
neuro push helloworld
```

After that, you can start the job by running:

```
neuro run image:helloworld
```

### How to Kill All Running Jobs

To kill all jobs that are currently running on your behalf, run the following command:

```
 neuro kill `neuro -q ps -o <user>`
```

For example,

```
 neuro kill `neuro -q ps -o mariyadavydova`
```

### How to Run Two or More Commands In a Job

Sometimes you want to execute two or three commands in a job without having to connect to it. For example, you may want to change the working directory and to run training. To achieve this, you need to wrap your commands in `”bash -c ‘<commands>’”` call, like this:

```
"bash -c 'cd /project && python mnist/train.py'"
```

### How to Get Output from a Running Job

There are two ways to get the output of your running job:

* Run it without the `--detach` option.
* Connect to a running job output with `neuro log <JOB>`, where JOB is either the id or the name of your job.

In some cases, Python caches the output of the scripts, so that you won’t get any output until the job finishes. To overcome this problem, provide `-u` option to `python`, like this:

```
"bash -c 'cd /project && python -u mnist/train.py'"
```



---
File: /docs/getting-started/references.md
---

# References

This table provides links to key resources for the Apolo platform, including documentation of various tools and components.

| Name               | Link                                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Apolo CLI          | [https://docs.apolo.us/index/apolo-cli](https://docs.apolo.us/index/apolo-cli)                                                             |
| Apolo Flow         | [https://docs.apolo.us/index/apolo-flow-reference](https://docs.apolo.us/index/apolo-flow-reference)                                       |
| Apolo Extras       | [https://docs.apolo.us/index/apolo-extras-cli](https://docs.apolo.us/index/apolo-extras-cli)                                               |
| Apolo Actions      | [https://docs.apolo.us/index/apolo-actions-reference](https://docs.apolo.us/index/apolo-actions-reference)                                 |
| Python SDK         | [https://docs.apolo.us/index/apolo-python-sdk](https://docs.apolo.us/index/apolo-python-sdk)                                               |
| Apolo Docker Image | [https://docs.apolo.us/index/getting-started/apolo-base-docker-image](https://docs.apolo.us/index/getting-started/apolo-base-docker-image) |




---
File: /docs/getting-started/troubleshooting.md
---

# Troubleshooting

## Lost/unknown job ID

The first step in any investigation is knowing a job ID. If you started your job with `apolo run`, the job's ID was printed in the output.

However, if you can't find the initial terminal output, you can use one of these commands to find a specific job:

{% tabs %}
{% tab title="apolo CLI" %}
Note: `apolo ps` is a shortcut for `apolo job ls`

`apolo ps` prints only running jobs.\
`apolo ps -a` prints all jobs.\
`apolo ps -s failed` prints all jobs with the Failed status.
{% endtab %}

{% tab title="apolo-flow" %}
Run `apolo-flow ps` to get the list of all jobs defined in a flow.
{% endtab %}
{% endtabs %}

## Image build failed

When you run `apolo-flow build IMAGE_NAME`, apolo-flow uploads the build context to the platform and creates a platform job that uses [Kaniko](https://github.com/GoogleContainerTools/kaniko) to build a docker image and push it to the platform registry.

If building fails, you can check the job's status and logs to get more information.

#### Getting a job's status

To check a job's status, run:

```
apolo status <job-ID> 
```

The **Status transitions** section in the output can help you learn at which step the job failed.

#### Getting builder logs

To check builder logs, run:

```
apolo logs <job-ID> 
```

## apolo run / apolo-flow run failed

There are a few main reasons your job may fail. Here are some of the most common:

#### Incorrect image name

This can happen if you have a typo in the image name or if the specified image was not built before running a job. List of all images can be accessed by running `apolo image ls`. You can also list tags for a particular image via `apolo image tags <IMAGE_URI>`.

#### Incorrect volume mounted

You might have an invalid volume mounted to the job. For example, you've mounted a volume to the `/my-project` folder, but your code expects `/my_project`. You can double-check it in the logs.

#### Cluster scale up failed

If you see a **Cluster Scale Up Failed** error in the status, it usually means you’ve requested resources that are not available in the cluster at the moment. For example, all GPUs are busy, so your job can’t be scheduled.

#### Code issues

You may have an error in your python script that prevents the job from running properly.

## Can’t access my job via HTTP

There are a few steps to troubleshooting such issues.

#### Checking for an open HTTP port

The first point of interest is whether you have an open HTTP port for your job. To check this, you can:

{% tabs %}
{% tab title="apolo CLI" %}
Use the `--http_port` parameter.
{% endtab %}

{% tab title="apolo-flow" %}
Use the `http_port:` option.
{% endtab %}
{% endtabs %}

#### Checking the listening IP

Next, make sure that your web app listens on 0.0.0.0, not on 127.0.0.1 or `localhost` — otherwise it won't be able to accept incoming requests from the outside of the container.

#### Disabling HTTP authentication

And finally, if you can access your job via browser, but `curl` and similar tools don’t work, most likely you didn’t disable HTTP authentication. The Apolo platform puts an HTTP authentication layer in front of your app by default for security reasons.

You can disable this behavior manually when running jobs:

{% tabs %}
{% tab title="apolo CLI" %}
Use the `--no-http-auth` parameter.
{% endtab %}

{% tab title="apolo-flow" %}
Use the `http_auth: False` option.
{% endtab %}
{% endtabs %}

## Troubleshooting a running job

Just like with Docker, you can get a shell in a running job to check its state. To do this, run:

```
apolo exec JOB_ID -- /bin/sh
```

Note: In Docker you would typically add the `-it` parameters to the command, but they’re not necessary for `apolo exec`.

## Navigating job statuses

A job might have one of the following statuses:

| Status        | Description                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **pending**   | The job is being created and scheduled. This includes finding (and possibly waiting for) sufficient amount of resources, pulling an image from a registry, etc. |
| **suspended** | The job's execution was temporarily suspended                                                                                                                   |
| **running**   | The job is running                                                                                                                                              |
| **succeeded** | The job terminated with the exit code _0_                                                                                                                       |
| **cancelled** | The running job was manually terminated/deleted                                                                                                                 |
| **failed**    | The job terminated with a non-_0_ exit code.                                                                                                                    |

Each of these statuses have additional sub-statuses that can help you monitor the job and trace errors on an more granular level:

| Sub-status           | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| PodInitializing      | Initializing a pod for the job                                            |
| ContainerCreating    | Creating a container for the job                                          |
| ErrImagePull         | Failed to pull the specified image                                        |
| ImagePullBackOff     | Stopping image pulling                                                    |
| InvalidImageName     | Incorrect image name was specified                                        |
| OOMKilled            | Job terminated due to an Out Of Memory error                              |
| Completed            | Job is completed                                                          |
| Error                | An error occured                                                          |
| ContainerCannotRun   | Cannot run the container                                                  |
| Creating             | Creating the job                                                          |
| Collected            | Job collected                                                             |
| Scheduling           | Scheduling the job execution                                              |
| NotFound             | The job could not be scheduled or was preempted                           |
| ClusterNotFound      | Specified cluster was not found                                           |
| ClusterScalingUp     | Scaling up                                                                |
| ClusterScaleUpFailed | Failed to scale up the cluster                                            |
| Restarting           | Restarting the job                                                        |
| DiskUnavailable      | Specified disk is currently unavailable                                   |
| QuotaExhausted       | User quota was exhausted - you will need to renew it to perform more jobs |
| LifeSpanEnded        | The job has reached the end of its lifespan                               |
| UserRequested        | The job was terminated per user request                                   |

##



---
File: /docs/README.md
---

# Introduction

[Apolo](https://apolo.us) is a flexible and robust machine learning platform.

If you're new to Apolo, here are two simple steps to get started:

* [Sign up](https://console.apolo.us) and contact [start@apolo.us](mailto:start@apolo.us) for potential collaboration or free trial.
* Follow our [Getting Started](getting-started/first-steps/getting-started.md) guide.

{% hint style="info" %}
To get more help, refer to the [FAQ](getting-started/faq.md) or contact us at [support@apolo.us](mailto:support@apolo.us)
{% endhint %}



---
File: /docs/SUMMARY.md
---

# Table of contents

## Getting started

* [Introduction](README.md)
* [First Steps](getting-started/first-steps/README.md)
  * [Getting Started](getting-started/first-steps/getting-started.md)
  * [Training Your First Model](getting-started/first-steps/training-your-first-model.md)
  * [Running Your Code](getting-started/first-steps/running-your-code.md)
* [Apolo Base Docker image](getting-started/apolo-base-docker-image.md)
* [FAQ](getting-started/faq.md)
* [Troubleshooting](getting-started/troubleshooting.md)
* [References](getting-started/references.md)

## Apolo Console

* [Getting started](apolo-console/getting-started/README.md)
  * [Sign Up, Login](apolo-console/getting-started/sign-up-login.md)
  * [Organizations](apolo-console/getting-started/organizations.md)
  * [Clusters](apolo-console/getting-started/clusters.md)
  * [Projects](apolo-console/getting-started/projects.md)
* [Apps](apolo-console/apps/README.md)
  * [Pre-installed apps](apolo-console/apps/pre-installed/README.md)
    * [Files](apolo-console/apps/pre-installed/files.md)
    * [Buckets](apolo-console/apps/pre-installed/buckets.md)
    * [Disks](apolo-console/apps/pre-installed/disks.md)
    * [Images](apolo-console/apps/pre-installed/images.md)
    * [Secrets](apolo-console/apps/pre-installed/secrets.md)
    * [Jobs](apolo-console/apps/pre-installed/jobs/README.md)
      * [Remote Debugging with PyCharm Professional](apolo-console/apps/pre-installed/jobs/remote-debugging-with-pycharm-professional.md)
      * [Remote Debugging with VS Code](apolo-console/apps/pre-installed/jobs/remote-debugging-with-vs-code.md)
    * [Flows](apolo-console/apps/pre-installed/flows.md)
  * [Available apps](apolo-console/apps/available-apps/README.md)
    * [Terminal](apolo-console/apps/available-apps/terminal.md)
    * [LLM Inference](apolo-console/apps/available-apps/llm-inference/README.md)
      * [vLLM Inference details](apolo-console/apps/available-apps/llm-inference/vllm-inference-details.md)
      * [Multi-GPU Benchmarks Report](apolo-console/apps/available-apps/llm-inference/multi-gpu-benchmarks-report.md)
    * [PostgreSQL](apolo-console/apps/available-apps/postgre-sql.md)
    * [Text Embeddings Inference](apolo-console/apps/available-apps/text-embeddings-inference.md)
    * [Jupyter Notebook](apolo-console/apps/available-apps/jupyter-notebook.md)
    * [Jupyter Lab](apolo-console/apps/available-apps/jupyter-lab.md)
    * [VS Code](apolo-console/apps/available-apps/vs-code.md)
    * [PyCharm Community Edition](apolo-console/apps/available-apps/py-charm.md)
    * [ML Flow](apolo-console/apps/available-apps/ml-flow.md)
    * [Apolo Deploy](apolo-console/apps/available-apps/apolo-deploy.md)
    * [Dify](apolo-console/apps/available-apps/dify.md)
    * [Weaviate](apolo-console/apps/available-apps/weaviate.md)
    * [Fooocus](apolo-console/apps/available-apps/fooocus.md)
    * [Stable Diffusion](apolo-console/apps/available-apps/stable-diffusion.md)

## Apolo CLI <a href="#apolo-concepts-cli" id="apolo-concepts-cli"></a>

* [Installing CLI](apolo-concepts-cli/installing.md)
* [Apps](apolo-concepts-cli/apps/README.md)
  * [Files](apolo-concepts-cli/apps/files.md)
  * [Jobs](apolo-concepts-cli/apps/jobs.md)
  * [Images](apolo-concepts-cli/apps/images.md)

## Administration

* [Overview and Installation](administration/overview-and-installation/README.md)
  * [Architecture Overview](administration/overview-and-installation/architecture-overview.md)
  * [On-premise Installation Guide](administration/overview-and-installation/on-premise-installation-guide.md)
* [Cluster Management](administration/cluster-management/README.md)
  * [Creating a Cluster](administration/cluster-management/creating-a-cluster.md)
  * [Managing Users and Quotas](administration/cluster-management/managing-users-and-quotas.md)
  * [Managing organizations](administration/cluster-management/managing-organizations.md)
  * [Creating Node Pools](administration/cluster-management/creating-node-pools.md)
  * [Managing Presets](administration/cluster-management/managing-presets.md)



---
File: /use-cases/.gitbook/assets/Reasoning_Framework.md
---

Directory Structure:

└── ./
    ├── sub-pages
    │   ├── How can we use existing reasoning models and where do they fit in the process.md
    │   ├── Multi-Phased Execution Plan.md
    │   ├── Paper to domain mapping.md
    │   ├── Reasoning Datasets.md
    │   ├── Reasoning Framework Viability.md
    │   └── Service Breakdown.md
    └── Reasoning Framework: Building an Open, Modular System for Advanced LLM Reasoning.md


---
File: /sub-pages/How can we use existing reasoning models and where do they fit in the process.md
---

# How can we use existing reasoning models and where do they fit in the process

Below is a more practical “mapping” from each of the open- or semi-open “o1-like” systems (including OpenAI-o1, DeepSeek-R1, and so forth) onto the four-service framework—**Policy Initialization**, **Reward Design**, **Search**, and **Learning**—plus some indication of which referenced approaches they’re using or could use. For each model, we’ll point out how it might plug into one or more of these “services” and what references or methods it appears to draw upon or could draw upon.

---

## 1. Policy Initialization

### 1.1 OpenAI-o1

- **Likely Approach**:
    1. **Massive Pre-training** (à la GPT-style).
    2. **Instruction Fine-Tuning** (c.f. Wei et al. 2022a [FLAN], Ouyang et al. 2022 [ChatGPT], etc.).
    3. **Human-like Reasoning Behaviors**: We see traces of problem decomposition, reflection, self-correction, etc.
- **How**:
    - They presumably started with a large base LLM (like GPT-3.5 or GPT-4 style) then used supervised fine-tuning on carefully curated data with chain-of-thought.
    - They heavily emphasize *reinforcement learning from human feedback* (RLHF) for alignment.

### 1.2 DeepSeek-R1

- **Likely Approach**:
    1. Also a large pre-trained base.
    2. Possibly “Self-Instruct” or RLHF style to produce chain-of-thought or “deep-seeking” solutions.
- **How**:
    - They could incorporate “Task Decomposition” and “Reflection” behaviors (like Madaan et al. 2023, Self-Refine) directly in the prompt or from instruction-tuned data.
    - Not fully open-sourced, so we only know that they highlight advanced reasoning on math/coding tasks.

### 1.3 Others (Marco-o1, o1-coder, etc.)

- **Marco-o1**:
    - *Base* is usually an open checkpoint (like LLaMA family).
    - They add a small amount of supervised fine-tuning with instruct data + partial solutions from search.
- **o1-coder**:
    - Focuses on code generation, so pre-training is likely code-heavy (like CodeLLaMA or an instruct-tuned coder model).
    - Also includes specialized data for debugging and multi-step code reasoning.

**References**:

- For code or math domain pretraining, see Chen et al. (2021), Fan et al. (2022), etc.
- For instruction tuning: Wei et al. (2022a), Chung et al. (2024), Taori et al. (2023), etc.
- For injecting “human-like reasoning behaviors,” see Bursztyn et al. (2022) for decomposition, Weng et al. (2023) for self-verification, etc.

---

## 2. Reward Design

### 2.1 OpenAI-o1

- **Likely Approach**:
    - A large suite of *preference-based* data (Christiano et al. 2017, Stiennon et al. 2020) for alignment.
    - *Outcome rewards* for tasks with known solutions (like math or coding).
    - *Process-level feedback* for deeper chain-of-thought correctness (Lightman et al. 2024 mentions step-level verifying).
- **How**:
    - They combine RLHF from crowdworkers (preference labeling or deeper textual feedback) plus some environment-based signals (e.g., code execution, math verification).
    - Possibly advanced “reward shaping” (Ng et al. 1999) to turn final correctness into dense signals for intermediate steps.

### 2.2 DeepSeek-R1

- **Likely Approach**:
    - Probably outcome-based or partial step-based verification for coding/math tasks (like Dou et al. 2024 or Chen et al. 2024c).
    - Possibly a *preference model* trained on how “deep” the chain-of-thought is or how “explanatory” it is.
- **How**:
    - If specialized in “deep seeking” problem solving, they might measure solution complexity or thoroughness.
    - Could use standard test-case or symbolic-checker reward signals in code/math domains.

### 2.3 Others

- **o1-journey**: The first part used a *process reward* for partial math solutions. The second part did more distillation from an existing model.
- **Open-Reasoner**: Uses “verifier-based RL,” akin to a reward model that checks correctness.
- **Slow Thinking with LLMs**: Also trains a “verifier” or “process reward” model to evaluate partial steps.

**References**:

- For environment-based (code, math), Dou et al. (2024), Shojaee et al. (2023), Zhang et al. (2024e).
- For preference-based RLHF, Christiano et al. (2017), Bai et al. (2022a), Stiennon et al. (2020).
- For shaping with partial correctness, Lightman et al. (2024), Setlur et al. (2024).

---

## 3. Search

### 3.1 OpenAI-o1

- **Likely Approach**:
    - Large-scale search at *train-time* and more “thinking” at *test-time*.
    - Possibly a “Best-of-N” or partial tree expansion strategy.
    - Evidence from their blog that “longer chain-of-thought” and “trial and error” helps.
- **How**:
    - They might do something akin to MCTS on certain tasks (like code or game-like logic) or simpler large-sample Best-of-N with a reward model.
    - At inference, they do “sequential revision” or “self-correction” in the multi-turn chat style.

### 3.2 DeepSeek-R1

- **Likely Approach**:
    - Emphasizes searching for more complex or deeper solutions. Possibly repeated sampling or partial expansions.
    - Could be a BFS/DFS (Yao et al. 2023a “Tree of Thought”) or ReACT-like (Yao et al. 2023b) approach.
- **How**:
    - They present partial reasoning steps, get environment feedback (like code or math checking), then refine.

### 3.3 Others

- **Open-Reasoner**: Monte Carlo Tree Search (MCTS) is used to improve final solutions.
- **o1-journey (Part 1)**: Beam search to generate partial solutions, then the best partial solutions are refined by GPT-4.
- **Slow Thinking with LLMs**: MCTS or “iterative self-correcting.”
- **Marco-o1**: MCTS + partial reflection at each step.
- **o1-coder**: MCTS specialized for coding tasks (compilation-based reward).

**References**:

- Best-of-N: Brown et al. (2024), Cobbe et al. (2021).
- MCTS: Silver et al. (2016), Wan et al. (2024), Chen et al. (2024a).
- Sequential Revision: Madaan et al. (2023), Shinn et al. (2023).
- Tree-of-Thought: Yao et al. (2023a).

---

## 4. Learning (Reinforcement or Distillation)

### 4.1 OpenAI-o1

- **Likely Approach**:
    1. **RLHF**: Probably a PPO-based pipeline (Ouyang et al. 2022 style).
    2. Possibly also **DPO** (Rafailov et al. 2023) or a custom actor-critic for chain-of-thought signals.
- **How**:
    - They gather solutions from the policy (with or without search).
    - Label them with a reward model (or direct human ranking).
    - Do repeated RL updates that steadily align policy with higher-reward solutions.

### 4.2 DeepSeek-R1

- **Likely Approach**:
    - Could rely partly on **Behavior Cloning** if they produce high-quality solutions. Possibly combined with preference-based RL.
    - The name suggests heavier usage of RL to push “deep seeking” search strategies.

### 4.3 Others

- **Open-Reasoner**: PPO or a variant during training, plus MCTS data for partial solutions.
- **Slow Thinking with LLMs**: They do DPO or SFT on solutions produced by MCTS (two technical reports).
- **o1-journey (Part 1)**: “Expert iteration” style—beam search → refine with GPT-4 → SFT.
- **o1-journey (Part 2)**: Distilling hidden chain-of-thought from a strong but “private” teacher (like Qwen-72B or o1-mini).
- **Marco-o1**: MCTS → SFT. Possibly introduces partial reflection to produce more curated data.
- **o1-coder**: MCTS for code, then supervised fine-tuning.

**References**:

- PPO: Schulman et al. (2017), Ouyang et al. (2022).
- DPO: Rafailov et al. (2023), Xie et al. (2024).
- Behavior Cloning & Expert Iteration: Silver et al. (2017) (AlphaGo Zero), Zelikman et al. (2022) (STaR), Touvron et al. (2023) (LLaMA 2).

---

## Putting It All Together

1. **OpenAI-o1**
    - **Policy Init**: Big LLM pretraining + instruction finetuning + unlocking reflection behaviors.
    - **Reward Design**: Large preference data (RLHF) + environment checks for tasks.
    - **Search**: Possibly sampling-based or partial tree expansions to generate high-quality data.
    - **Learning**: PPO or a similar RL approach from that data.
2. **DeepSeek-R1**
    - **Policy Init**: Possibly also big pretraining + instruction tuning.
    - **Reward Design**: For deep solutions, they might rely on environment (math/coding) or a custom “depth” measure.
    - **Search**: Emphasizes iterative expansions, possibly BFS or MCTS with feedback.
    - **Learning**: Some combination of BC on “deep solutions” plus RL to push exploration.
3. **Others** (like o1-journey, Open-Reasoner, Slow Thinking with LLMs)
    - They mix and match:
        - *Train-time search* (Beam or MCTS), or *test-time search* (self-correction, BFS).
        - *Reward modeling* (verifier or preference).
        - *Learning* via BC (expert iteration) or RL (PPO, DPO).

Thus, each “service” in your framework—Policy Initialization, Reward Design, Search, and Learning—can be “activated” by the relevant references or approaches these projects used. Different combinations yield the various “o1-like” pipelines we see.


---
File: /sub-pages/Multi-Phased Execution Plan.md
---

# Multi-Phased Execution Plan (Reasoning Framework)

Below is a proposed multi-phased, iterative roadmap to build and validate a “reasoning framework” along the lines of the blueprint we’ve been discussing. Each phase has tangible deliverables, and each step unlocks further functionality for training and deploying reasoner models. The plan assumes you start with a certain baseline LLM (or multiple LLMs you want to experiment with).

---

## **Phase 0: Foundations and Setup**

1. **Infrastructure & Environment Setup**
    - **Deliverable**: A minimal pipeline that can host your chosen model (e.g., LLaMA, Falcon, or GPT-style) and run text-in/text-out.
    - **Tasks**:
        - Configure GPU/accelerator environment.
        - Wrap model in a standard API (e.g., “generate tokens,” “get log probabilities”) so you can do more advanced operations later.
2. **Dataset Ingestion & Management**
    - **Deliverable**: A data pipeline for reading/writing multiple dataset formats (math, code, instruction data, etc.).
    - **Tasks**:
        - Download relevant open datasets (e.g., MATH, GSM8K, FLAN, code sets).
        - Create a uniform structure: e.g., JSON lines with `{"prompt": "...", "solution": "...", "reward": X}` or similar.

**Why do this first?**

Because every service—Policy Init, Reward, Search, Learning—depends on a functioning environment and consistent dataset handling.

---

## **Phase 1: Policy Initialization**

**Objective**: Produce a “strong enough” base policy capable of multi-step reasoning behaviors like “think aloud,” “reflect,” or “decompose tasks,” at least in a basic sense.

1. **Instruction Fine-Tuning**
    - **Deliverable**: A single-turn instruction-tuned checkpoint.
    - **Tasks**:
        - Fine-tune your base LLM on open instruction data (e.g., FLAN, Super-NaturalInstructions, Alpaca, etc.).
        - Validate that it can follow basic instructions or short tasks.
2. **Chain-of-Thought / Reasoning Behaviors**
    - **Deliverable**: A refined checkpoint that can produce step-by-step solutions or “reflect” in some manner.
    - **Tasks**:
        - Option 1: **Supervised Fine-Tuning** on chain-of-thought style data (like “explanations” from MATH, GSM8K).
        - Option 2: **Prompt Engineering** to see if the model already supports “self-check,” “analyze,” or “decompose.”
    - **Verification**: Evaluate on small math or logic tasks. Confirm that the model can produce a multi-step reasoning output.
3. **Intermediate Checkpoint**
    - **Deliverable**: “InitPolicy-v1” – a single standard checkpoint that we’ll use for the next phases.

**Why do this now?**

We want a workable initial policy before advanced RL or search. If it can’t even produce coherent multi-step text, it’s tough to do more.

---

## **Phase 2: Basic Search Module**

**Objective**: Implement a *search wrapper* that can sample multiple solutions or step expansions, orchestrating calls to the model’s text generation.

1. **Best-of-N (BoN) Search**
    - **Deliverable**: A small library that, given a prompt, samples N solutions from the policy, and uses *some* scoring method (e.g., perplexity or a naive “verifier”) to pick the best.
    - **Verification**: Compare “BoN pass@1” vs. “single-sample pass@1” on, e.g., math tasks. Show improvement.
2. **Beam Search**
    - **Deliverable**: A beam-search-based decoding that prunes or expands partial sequences.
    - **Tasks**:
        - Add hyperparameters: beam size, length penalty, etc.
        - Possibly allow a small user-provided function (e.g., partial step checking) to prune.
3. **Sequential Revision / Self-Refine** (Optional but Powerful)
    - **Deliverable**: A function that takes an initial model output, asks the model to critique or evaluate it, then produces a revised version—repeatedly.
    - **Verification**: Show improvement from “Refine x times” on a set of test prompts.

**End Result**:

You have an off-the-shelf “search service” that can be toggled between BoN, beam, or refinement. Even without advanced reward modeling, you can rely on naive heuristics or partial ground-truth checks to pick the best solution.

---

## **Phase 3: Reward Design & Integration**

**Objective**: Provide dense or outcome-based signals for tasks, so that the search and subsequent RL phases can rely on *real* reward feedback.

1. **Outcome-Based Reward**
    - **Deliverable**: A function that checks final solutions for correctness. Examples:
        - **Math**: Compare the final numeric answer to ground truth (MATH, GSM8K).
        - **Code**: Run the code snippet or test cases, check pass/fail.
    - **Verification**: *Search Integration* – let your search wrapper call this function automatically to pick or prune solutions.
2. **Process Reward** / Step-by-Step Labeling (Optional but recommended)
    - **Deliverable**: A custom “verifier” or “scoring model” that can examine partial reasoning steps.
    - **Tasks**:
        - Possibly train a step-level classifier on step-labeled data (Lightman et al. 2024) or hand-labeled partial math solutions.
        - Provide a numeric reward (e.g., +1 if a step is correct, 0 otherwise) to guide the search or RL more granularly.
3. **Preference-Based Reward (RLHF)**
    - **Deliverable**: A small “reward model” (RM) trained on preference-labeled outputs.
    - **Tasks**:
        - Collect (or re-use) pairs/triples of model outputs, each with a human or proxy ranking.
        - Train a Bradley-Terry or direct preference model.
    - **Verification**: *Check correlation with known correctness*. E.g., does the RM give highest scores to correct solutions?

At the end of Phase 3, we have a “Reward Service” that can plug into the search from Phase 2 (or future RL).

---

## **Phase 4: Advanced Search & Generation of Training Data**

**Objective**: Combine the “Search” from Phase 2 with the “Reward” from Phase 3 to systematically collect higher-quality data. This data is critical for the Learning (RL) step.

1. **Data Generation Runs**
    - **Deliverable**: A “search pipeline” that, for each problem in your dataset(s), runs e.g. MCTS or Best-of-N or self-refinement, obtains the highest-reward solution, and logs:
        - (prompt, partial steps, final solution, reward).
    - **Verification**: Confirm that the search pipeline is stable and can handle, say, 1k or 10k tasks.
2. **Scaling**
    - **Deliverable**: Rerun the above pipeline on larger sets (like MATH, code challenges, etc.) to produce enough examples of “search-improved solutions.”
    - **Why**: This data will be used to fine-tune or RL-train your model.

At this point, you have a method to produce new examples that are (on average) better than naive single-sample solutions. You also have the associated reward. This sets the stage for RL-based improvement.

---

## **Phase 5: Learning / RL or Distillation**

**Objective**: Actually *improve* the policy, using the search-generated data or environment interactions.

1. **Behavior Cloning (BC)**
    - **Deliverable**: A “BC pipeline” that takes the top solutions (highest reward) from Phase 4’s data and re-trains the policy to mimic them.
    - **Verification**: Evaluate the new policy’s pass@1 vs. the old policy. Show improvement.
2. **Policy Gradient (PPO, DPO, etc.)**
    - **Deliverable**: Optionally train the model with a policy gradient method on *all* solutions (including negative or partial).
    - **Tasks**:
        - Implement or adapt an open-source RLHF codebase (e.g., Hugging Face’s TRL) but hooking it up to your reward function.
        - Possibly do multiple epochs of RL, sampling new data from updated policy each time (online or “semi-online” approach).
    - **Verification**: Evaluate success metrics (math accuracy, code pass rate, or subjective preference).
3. **Iterate**
    - Possibly cycle back to Phase 4 with your improved policy, re-run search to gather even better data, and re-train. This is akin to AlphaGo Zero’s iterative “expert iteration.”

---

## **Phase 6: Test-Time Search & Packaging**

**Objective**: Expose the final “reasoning framework” to end users or downstream tasks in a flexible, robust way.

1. **Inference-Time Search**
    - Decide how you want to “package” search at inference:
        - Quick “Best-of-N sampling”?
        - Full-blown MCTS if you want maximum performance (but more compute)?
        - Self-refine loops with your final policy?
    - **Deliverable**: A “Reasoner API” that can be called with a user query and automatically runs whichever approach you pick.
2. **User-Facing API**
    - **Deliverable**: Possibly a REST or gRPC endpoint that orchestrates:
        1. The *final policy inference*.
        2. Optionally *search expansions* or *refinement steps*.
        3. Returning the best solution.
    - **Verification**: Beta test with real user queries.
3. **Logging & Monitoring**
    - Collect logs for user satisfaction or further training data.

---

## **Phase 7: Extensions & Refinements (Ongoing)**

**Objective**: Improve domain coverage, incorporate new tasks, or unify with multi-modality or real environment interaction.

1. **Domain-Specific Enhancements**
    - If you want to handle more complex tasks (e.g. specialized code generation in, say, Rust or a complicated math domain), you can re-run earlier phases with domain corpora.
2. **Multi-modal** (Optional)
    - Expand your “search” or “reward” logic to handle images or external tools (Hao et al. 2023 “Reasoning with LLM is Planning with World Model,” etc.).
3. **Iterate**
    - This entire plan can run in a loop. Each time you have more data or improved models, the search and learning can yield better performance.

---

## **Summary of Deliverables and Verification**

1. **Phase 0**: Working environment, consistent dataset pipeline.
2. **Phase 1**: Baseline “InitPolicy-v1” with instruction tuning + basic step-by-step reasoning.
3. **Phase 2**: Search module (BoN, beam, or sequential refine).
4. **Phase 3**: Reward design (outcome checks, preference model, optional step-level).
5. **Phase 4**: Automated data generation using Phase 2 + 3, storing (prompt, solution, reward).
6. **Phase 5**: Policy learning from that data (Behavior Cloning, PPO, etc.).
7. **Phase 6**: Production-grade reasoning API with optional search at inference.
8. **Phase 7**: Domain expansions, iteration, or multi-modality.

At each phase, you have a discrete deliverable (“We have a stable instruction model,” “We have a working search library,” “We have a reward function with known accuracy,” “We improved pass@1 from X to Y,” etc.), making each step verifiable and trackable. By phasing it out in this manner, you ensure incremental progress and can pivot or refine your approach based on real-world performance data.


---
File: /sub-pages/Paper to domain mapping.md
---

# Paper to domain mapping

Below is a grouped collection of references, organized by the four major “services” (or components) of the reasoning framework outlined in the paper: **(1) Policy Initialization**, **(2) Reward Design**, **(3) Search**, and **(4) Learning**. Under each heading, you’ll see papers that the paper itself references as crucial background or exemplars. These references can serve as a starting point to implement each respective “service” in your modular reasoner system.

---

## 1. **Policy Initialization**

### 1.1 Pre-Training and Basic LLM Capabilities

- **Radford & Narasimhan (2018)**, “Improving Language Understanding by Generative Pre-Training”
- **Radford et al. (2019)**, “Language Models are Unsupervised Multitask Learners”
- **Brown et al. (2020)**, “Language Models are Few-Shot Learners”
- **Lee et al. (2024)**, “Reasoning Abilities of Large Language Models: In-depth Analysis…”
- **Manning (2022)**, “Human Language Understanding & Reasoning”
- **Sun et al. (2024d)**, “A Survey of Neural Code Intelligence…” (pre-training on code)
- **Weber et al. (2024)**, “RedPajama: An Open Dataset for Training Large Language Models”
- **Liu et al. (2024f)**, “Datasets for Large Language Models: A Comprehensive Survey”
- **Kaplan et al. (2020)**, “Scaling Laws for Neural Language Models”
- **Hoffmann et al. (2022)**, “Training Compute-Optimal Large Language Models”

These are fundamental works behind modern large-scale pre-training, investigating how “basic” LLM capabilities emerge from massive, self-supervised training.

### 1.2 Instruction Fine-Tuning

- **Wei et al. (2022a)**, “Finetuned Language Models Are Zero-Shot Learners (FLAN)”
- **Chung et al. (2024)**, “Scaling Instruction-Finetuned Language Models”
- **Sanh et al. (2022)**, “Multitask Prompted Training Enables Zero-Shot Task Generalization”
- **Wang et al. (2022b)**, “Super-NaturalInstructions: Generalization via Declarative Instructions…”
- **Taori et al. (2023)**, “Stanford Alpaca”
- **Wang et al. (2023b)**, “Self-Instruct: Aligning Language Models with Self-Generated Instructions”
- **Hayati et al. (2024)**, “Chain-of-Instructions: Compositional Instruction Tuning on Large Language Models”

These papers focus on turning a generic LLM into an *instruction-following* or *user-aligned* system, vital for having “interactive” or “helpful” policies that can reason in a step-by-step manner.

### 1.3 Human-like Reasoning Behaviors

- **Lewkowycz et al. (2022)**, “Solving Quantitative Reasoning Problems with Language Models”
- **Yu et al. (2024b)**, “Thought Propagation: An Analogical Approach…” (basic emergent reasoning)
- **Kondrakunta et al. (2018)**, “Toward Problem Recognition, Explanation and Goal Formulation” (problem analysis)
- **Deng et al. (2023)**, “Prompting and Evaluating LLMs for Proactive Dialogues” (clarification behaviors)
- **Zhou et al. (2023a)**, “Least-to-Most Prompting…” (task decomposition)
- **Bursztyn et al. (2022)**, “Learning to Perform Complex Tasks through Compositional Fine-Tuning”
- **Gerwig et al. (2021)**, “The Relationship between Intelligence and Divergent Thinking” (alternative proposals)
- **Liang et al. (2024)**, “Encouraging Divergent Thinking in LLMs…” (alternative proposals)
- **Weng et al. (2023)**, “Large Language Models Are Better Reasoners with Self-Verification” (self-evaluation)
- **Bai et al. (2022b)**, “Constitutional AI: Harmlessness from AI Feedback” (self-check, RLHF)
- **Liu et al. (2024a)**, “LLMs Have Intrinsic Self-Correction Ability”
- **Zhang et al. (2024a)**, “Learning to Check… Unleashing Potentials for Self-Correction”

These show ways to embed behaviors like reflection, decomposing tasks, checking correctness, etc.—often via supervised fine-tuning or prompt designs.

---

## 2. **Reward Design**

### 2.1 Outcome Rewards vs. Process Rewards

- **Cobbe et al. (2021)**, “Training Verifiers to Solve Math Word Problems” (outcome-based correctness)
- **Shao et al. (2024)**, “DeepSeekMath: Pushing Limits of Math Reasoning in Open LMs” (outcome-based)
- **Lightman et al. (2024)**, “Let’s Verify Step by Step” (process reward, step-level correctness)
- **Yin et al. (2024a)**, “Aggregation of Reasoning: A Hierarchical Framework…” (process supervision)

### 2.2 Reward from Environment

- **Dou et al. (2024)**, “Self-Play with Execution Feedback: Code Generation” (compilation-based reward)
- **Fan et al. (2022)**, “MineDojo: Building Open-Ended Embodied Agents…” (environment as reward)
- **Shridhar et al. (2021)**, “ALFWorld…” (web or textual environment)

### 2.3 Reward Modeling from Data

### 2.3.1 Preference Data (RLHF / Bradley-Terry Models)

- **Christiano et al. (2017)**, “Deep RL from Human Preferences”
- **Stiennon et al. (2020)**, “Learning to Summarize from Human Feedback”
- **Bai et al. (2022a)**, “Training a Helpful and Harmless Assistant with RL from HF”
- **Rafailov et al. (2023 / 2024)**, “Direct Preference Optimization,” “From r to Q*…”

### 2.3.2 Inverse Reinforcement Learning

- **Ng & Russell (2000)**, “Algorithms for Inverse Reinforcement Learning”
- **Abbeel & Ng (2004)**, “Apprenticeship Learning via IRL”

### 2.4 Reward Shaping / Potential-Based Methods

- **Ng et al. (1999)**, “Policy Invariance under Reward Transformations”
- **Setlur et al. (2024)**, “Reward Shaping for LLM Reasoning (Potential-based shaping)”

### 2.5 Distribution Shift & Overoptimization

- **Gao et al. (2023)**, “Scaling Laws for Reward Model Overoptimization”
- **Stroebl et al. (2024)**, “Inverse Scaling Flaws in Large LM Resampling”

### 2.6 Value Function, Heuristics, etc.

- **Yu et al. (2024a)**, “OVM: Outcome-supervised Value Models…” (value-based guidance)
- **Chen et al. (2024a)**, “AlphaMath Almost Zero: Process Supervision…” (training value heads)
- **Yao et al. (2023a)**, “Tree-of-Thought: BFS/DFS with Heuristics”
- **Hao et al. (2023)**, “Reasoning with LLM is Planning with World Model” (heuristic guidance)

---

## 3. **Search**

### 3.1 Tree Search (Beam, Best-of-N, MCTS)

- **Cobbe et al. (2021)**, “Verifier-based Best-of-N”
- **Brown et al. (2024)**, “Large Language Monkeys: Scaling Inference Compute with Repeated Sampling (Best-of-N)”
- **Sun et al. (2024a)**, “Speculative Rejection: Accelerating Best-of-N”
- **Sessa et al. (2024)**, “BOND: Aligning LLMs with Best-of-N Distillation”
- **Amini et al. (2024)**, “Variational Best-of-N (vBoN)”
- **Xie et al. (2023)**, “Self-Evaluation Guided Beam Search”
- **Yu et al. (2024a)**, “Beam Search with Value Models”
- **Wan et al. (2024)**, “AlphaZero-like Tree Search for LLMs”
- **Liu et al. (2024c)**, “PPO-MCTS with LLMs”
- **Chen et al. (2024a)**, “AlphaMath: MCTS on Math Problems”
- **Zhang et al. (2023b)**, “Token-level MCTS for Program Generation”
- **Qi et al. (2024)**, “rStar: Combining Self-Consistency with MCTS”
- **Hao et al. (2023)**, “RAP: MCTS-based Planning”

### 3.2 Sequential Revisions

- **Madaan et al. (2023)**, “Self-Refine: Iterative Self-Correction”
- **Snell et al. (2024)**, “Comparing Sequential Revisions to BoN, Tree Search”
- **Shinn et al. (2023)**, “Reflexion: Language Agents with Verbal RL”
- **Chen et al. (2024c)**, “Self-Debug for Code Generation”
- **Gou et al. (2024)**, “Critic: LLMs Can Self-Correct with Tool-Interactive Critiquing”

### 3.3 Combination & Frameworks

- **Yao et al. (2023a)**, “Tree of Thought: DFS/BFS expansions with backtracking”
- **Koh et al. (2024)**, “A*-based Search for LLM Planning”
- **Lehnert et al. (2024)**, “Beyond A*: Search Dynamics Bootstrapping for Transformers”
- **Snell et al. (2024)**, “Scaling Test-Time Compute (Tree vs. Sequential vs. Model Size)”

---

## 4. **Learning** (Reinforcement or Iterative Fine-Tuning)

### 4.1 Policy Gradient, Actor-Critic, PPO

- **Sutton et al. (1999)**, “Policy Gradient Methods for RL” (REINFORCE)
- **Konda & Tsitsiklis (1999)**, “Actor-Critic Algorithms”
- **Schulman et al. (2015, 2017)**, “TRPO / PPO” (constraint-based RL training)
- **Li et al. (2024c)**, “Remax: A Simple, Effective RL Method for LLMs”
- **Shao et al. (2024)**, “GRPO: PPO Variation with Monte Carlo Baseline”
- **Zheng et al. (2023c)**, “Secrets of RLHF in LLMs (PPO Implementation Details)”

### 4.2 Direct Preference Optimization (DPO)

- **Rafailov et al. (2023 / 2024)**, “Direct Preference Optimization,” “From r to Q*…”
- **Xie et al. (2024)**, “Monte Carlo Tree Search + DPO (MCTS-DPO)”
- **Chen et al. (2024b)**, “Step-Level Value Preference Optimization for Math Reasoning”
- **Dubey et al. (2024)**, “The Llama 3 Herd of Models” (DPO for RLHF)
- **Zhong et al. (2024)**, “DPO Meets PPO: Reinforced Token Optimization”

### 4.3 Behavior Cloning / Expert Iteration

- **Zelikman et al. (2022)**, “STaR: Bootstrapping Reasoning with Reasoning” (reject-sampling BC)
- **Chen et al. (2024a)**, “AlphaMath… (MCTS + BC on Top Solutions)”
- **Anthony et al. (2017)**, “Expert Iteration”
- **Silver et al. (2017)**, “AlphaGo Zero” (MCTS + Behavior Cloning)
- **Wan et al. (2024)**, “TS-LLM: MCTS + BC”
- **Touvron et al. (2023)**, “LLaMA 2” (STaR-like iterative approach)

### 4.4 Scaling Laws, Distribution Shift, etc.

- **Brown et al. (2024)**, “Scaling Inference Compute with Repeated Sampling (best-of-n pass rates)”
- **Gao et al. (2023)**, “Scaling Laws for RM Overoptimization” (inverse scaling risk)
- **Huang et al. (2022)**, “The 37 Implementation Details of PPO” (implementation specifics)
- **Tuyls et al. (2024)**, “Scaling Laws for Imitation Learning (Atari context)”

---

### How to Use These Groupings

- **Policy Initialization** references are invaluable for building or refining the *base model* (pretraining, instruction tuning, and injecting step-by-step or “human-like” reasoning).
- **Reward Design** references show how to create outcome or process rewards, handle preference learning, do inverse RL, or tackle shaping and distribution-shift concerns.
- **Search** references provide blueprint algorithms (Best-of-N, beam search, MCTS, sequential revision) and expansions for bridging “thinking more” at inference or train-time data collection.
- **Learning** references cover the main RL algorithms (PPO, DPO, etc.) and behavior cloning approaches to incorporate the newly generated data/trajectories into the policy’s weights.

Taken together, these papers give a rich literature basis for *each service* you’d want to implement in a modular reasoner framework.


---
File: /sub-pages/Reasoning Datasets.md
---

# Reasoning Datasets

Below is a grouping of **open reasoning datasets** mentioned or implied in the paper (or its references), along with suggestions on *where* in the four-service pipeline they typically fit. Some datasets can be relevant to more than one stage—e.g., a math dataset might help with both supervised instruction tuning and RL-based fine-tuning. But this categorization shows their *most common uses* in a reasoning-focused workflow.

---

## 1. Policy Initialization Datasets

These are datasets people often use to **pre-train** or **instruction-tune** models, giving them a general “reasoning” or “instruction-following” capability right off the bat.

1. **FLAN Instruction Data (Wei et al. 2022a)**
    - *What it is*: A broad collection of tasks cast as instructions (“finetuned language models are zero-shot learners”).
    - *Open?*: Yes, FLAN is publicly available.
    - *Where it fits*:
        - **Instruction Fine-Tuning** for policy initialization, so the model learns to follow and solve multiple instruction types.
2. **Super-NaturalInstructions (Wang et al. 2022b)**
    - *What it is*: A large suite (1,600+ tasks) framed as instructions.
    - *Open?*: Yes, publicly released.
    - *Where it fits*:
        - **Instruction Fine-Tuning** to expand the model’s coverage of tasks and reasoning formats.
3. **Self-Instruct (Wang et al. 2023b)**
    - *What it is*: A method/dataset where an LLM itself generates new tasks and solutions to increase instruction diversity.
    - *Open?*: Yes, the pipeline and examples are open-sourced.
    - *Where it fits*:
        - **Instruction Fine-Tuning** for a broader variety of user queries and step-by-step instructions.
4. **Alpaca (Taori et al. 2023)**
    - *What it is*: 52K instruction–response pairs generated from GPT and used to fine-tune smaller LLMs.
    - *Open?*: Yes (the dataset is on GitHub, though the underlying GPT calls are subject to original disclaimers).
    - *Where it fits*:
        - **Instruction Fine-Tuning** (policy init), often with short to moderately complex instructions.
5. **Code or Math Pretraining Corpora**
    - E.g., [Code-based corpora](https://github.com/openai/human-eval) for code LLMs; [Math texts or “ArXiv math” data] used in some projects.
    - *Open?*: Many large code repositories are partially open, and math text corpora (arXiv, StackExchange dumps) exist.
    - *Where it fits*:
        - **Pre-Training** or specialized domain training (e.g., code or math) so that the model is well-initialized for advanced reasoning in code or symbolic math.

---

## 2. Reward Design Datasets

Datasets that help train a *reward model* or *verifier*, or provide ground-truth signals for outcome-based reward. Many are “annotated for correctness” or “paired preference data,” so they’re used in **Reward Modeling**.

1. **Preference Data (Human Rankings)**
    - *Generic RLHF Setup*: Collect pairs or sets of answers, each with a human ranking.
    - *Open?*: Partially; some RLHF datasets exist but are not always fully released. OpenAssistant, Anthropic HH data, etc., have partial releases.
    - *Where it fits*:
        - **Reward Modeling** from preference data for alignment (Christiano et al. 2017, Stiennon et al. 2020).
2. **MATH (Cobbe et al. 2021)**
    - *What it is*: A dataset with 12K competition-level math problems; each has a “ground-truth” solution.
    - *Open?*: Yes (GitHub: “openai/MATH”).
    - *Where it fits*:
        - **Outcome Reward** for math correctness (0/1) if the final answer matches the reference.
        - Can also be used to train a *verifier model* that checks partial solutions for correctness (Lightman et al. 2024).
3. **GSM8K**
    - *Not explicitly named in the paper’s references but heavily used in the LLM community.*
    - *What it is*: ~8K grade-school math problems with solutions.
    - *Open?*: Yes.
    - *Where it fits*:
        - Same function as MATH: *Outcome-based reward* or *verifier training*.
4. **ALFWorld / AlfWorld Data (Shridhar et al. 2021)**
    - *What it is*: An environment+dataset bridging text instructions and environment states.
    - *Open?*: Yes, on GitHub.
    - *Where it fits*:
        - **Environment-based Reward**: Use logs from ALFWorld or the environment itself to train a reward model that says “success/fail” for certain actions.
5. **MineDojo (Fan et al. 2022)**
    - *What it is*: A simulation environment + tasks for open-ended Minecraft-based reasoning.
    - *Open?*: Yes, publicly available.
    - *Where it fits*:
        - **Reward Design**: Environment returns success signals (did you build X?), so you can train or shape a reward model to replicate environment feedback.

---

## 3. Search Datasets

Here we mean “datasets or tasks commonly used to **evaluate** or **drive** search-based strategies (like MCTS, Best-of-N, or BFS).” Often, they are test sets with known solutions, letting you test if search can find them.

1. **MATH (Cobbe et al. 2021)** again
    - Because MATH problems have known solutions, they’re used to test multi-step search.
    - *Where it fits*:
        - **Search**: The model can do MCTS or BFS, then compare to ground truth.
2. **Code Challenges (e.g., HumanEval, MBPP, APPS)**
    - *HumanEval* (Chen et al. 2021): 164 coding tasks with ground truth.
    - *MBPP* (Austin et al. 2021): ~1k code problems.
    - *APPS* (Hendrycks et al. 2021): ~10k programming challenges.
    - *Open?*: Yes, widely used, with public GitHubs.
    - *Where it fits*:
        - **Search**: Evaluate whether multi-sample or MCTS-based code generation hits correct solutions (pass@N metric).
3. **“Step-checking” or “Process Supervision”**
    - Datasets that contain partial solutions with correctness tags (Lightman et al. 2024). Not all are fully open, but some math subsets or hand-labeled step data exist.
    - *Where it fits*:
        - **Search**: You can incorporate partial-check feedback to prune search branches.

---

## 4. Learning (Reinforcement / Distillation) Datasets

Some open sets are used specifically to **train** or **finetune** an LLM in a reinforcement loop or an expert-distillation loop (e.g., “Expert Iteration” style).

1. **MATH** or **GSM8K** (again)
    - Because you have ground truth or partial step correctness, you can do *Behavior Cloning from correct solutions* or *PPO w.r.t. final correctness.*
    - *Where it fits*:
        - **Learning** (RL or supervised) from environment-labeled correctness.
2. **Self-Refine Data** (Madaan et al. 2023)
    - The “SELF-REFINE” approach can produce a dataset of “(initial draft → self-feedback → refined draft).”
    - *Open?*: The approach is open-sourced, though the final curated data might vary.
    - *Where it fits*:
        - **Behavior Cloning** from refined solutions or partial preference data for RL.
3. **STaR (Zelikman et al. 2022)**
    - *What it is*: A process of generating solutions and automatically filtering correct ones to build a curated fine-tuning set.
    - *Open?*: The methodology is described; actual code and instructions are partially open.
    - *Where it fits*:
        - **Learning**: Expert iteration or iterative BC. The dataset is effectively “LLM’s correct self-solutions.”
4. **Open-Source RLHF Datasets**
    - Projects like **OpenAssistant** or **LAION** have partially open preference data.
    - *Where it fits*:
        - **Learning**: Pair it with PPO, DPO, or other RL on top of your policy.

---

## Summary: Where These Datasets “Slot In”

- **Policy Initialization**
    - *Instruction-based data* (FLAN, Super-NaturalInstructions, Self-Instruct, Alpaca)
    - *Domain pretraining corpora* for math or code.
- **Reward Design**
    - *Human preference sets* (OpenAssistant, Anthropic HH, etc.)
    - *Environment-labeled sets* (ALFWorld, MineDojo) or code testers.
    - *Math or code correctness sets* (MATH, GSM8K) to build a “verifier.”
- **Search**
    - *Evaluation sets* that have a strong notion of correctness (MATH, code tasks like HumanEval, MBPP, APPS).
    - *Partial step-labeled data* if you do process-level expansions.
- **Learning (RL or BC)**
    - *Ground-truth reasoning tasks* (again MATH, GSM8K, code sets) for supervised or RL
    - *Self-generated correctness data* (Self-Refine, STaR)
    - *Open RLHF sets* for policy gradient or preference-based optimization.

Essentially, these open datasets (especially MATH, GSM8K, code sets, and large instruction collections) can serve double or triple roles. They might help with instruction finetuning (policy init), with building a reward model (if they have correctness or preference annotations), with search-based expansions (since you know the final ground-truth answers), and with final RL or BC.

Hence, the same dataset is often reused across multiple steps in the pipeline—what changes is *how* you use it (supervised fine-tuning vs. training a reward model vs. verifying search outputs, etc.).


---
File: /sub-pages/Reasoning Framework Viability.md
---

# Reasoning Framework Viability

It’s to build a system that any organization (or individual) can “plug” a model into and get a reasoner-style LLM out of it. The key is designing each of the four components (policy initialization, reward design, search, and learning) in a *model-agnostic* way. Below are a few considerations that make it possible:

---

### 1. Model-Agnostic Interfaces

1. **Policy API**
    - To slot in *any* base LLM, you just need a uniform way to (a) provide prompts/contexts, (b) receive token-level or chunk-level outputs, and (c) possibly reset or backtrack for search.
    - This is typically easy if the model is accessible through a standard text completion or chat API.
2. **Reward API**
    - The system’s reward “service” shouldn’t assume anything special about *how* the model generates text, only that it can provide final or partial outputs.
    - For example, for math or code tasks, the reward service just runs the code or checks the solution. For alignment tasks, it runs a preference or compliance check.
    - That means you can plug in a Hugging Face model, an API-based model, or an in-house checkpoint—whatever can yield text.
3. **Search API**
    - The search logic (e.g., beam search, MCTS, self-reflection loops) can remain “one level above” the model, simply orchestrating calls to the model.
    - The search algorithm only needs the ability to “ask” the model for the next token/step/solution, then evaluate it.
4. **Learning/Fine-Tuning API**
    - If you have local access to weights (like open-source LLaMA/CodeLLaMA or Falcon), you can do RL or supervised fine-tuning.
    - If the model is closed-source and API-only, you could still do *some* “reward re-ranking” or “search-based distillation” externally, but you’re limited in how you actually retrain or update the base model.
    - The more control you have over the model’s parameters, the more you can do deep RL.

---

### 2. Uniform “Blueprint” with Swappable Modules

Given these interfaces, you can design a single “blueprint”:

1. **Initialization**:
    - Let the user specify how they want to build their base model or pass in an existing checkpoint.
    - Optionally allow them to do a small amount of supervised instruction tuning right in your pipeline.
2. **Reward Specification**:
    - A simple set of hooks for registering “how do I evaluate a candidate solution?” for different tasks.
    - Could be an environment-based function (execute code) or an LLM-based preference checker.
3. **Search**:
    - The user can choose from a drop-down: “Best-of-N sampling,” “beam search,” “MCTS,” “self-refine,” etc.
    - Provide step-by-step logs of the partial solutions and final picks.
4. **Learning**:
    - Let the user pick “Behavior Cloning,” “PPO,” or “DPO” if they’re training the model weights, or skip if the user only has black-box model access.
    - Possibly share or store the generated data so it can be leveraged for future finetuning.

If each of these steps is implemented behind uniform, well-defined APIs, *any model* that can handle “predict next token” calls (or “generate text from a prompt”) can fit into your reasoner system.

---

### 3. Challenges and Caveats

1. **Closed-Source vs. Open-Source**
    - If the model is fully open (like many open-source LLMs), you can integrate *all* the RL pieces (PPO, DPO, etc.).
    - If the model is only accessible through an API, your *learning* options may be limited to *reward re-ranking* or *search strategies*; true finetuning might not be possible.
2. **Efficiency**
    - Techniques like MCTS and repeated self-refinement can be expensive. Some large models will be slow for big iterative searches, so you might want to provide user-configurable trade-offs (e.g., limit expansions, prune aggressively).
3. **Data Governance**
    - Users might not want to share their own domain data (especially for code or proprietary math tasks). So each portion of the pipeline should handle data privacy carefully.

---

### Bottom Line

Yes, it’s *definitely* possible to build a “reasoner framework” that any user can attach an LLM to in order to get advanced inference (search) and iterative improvement (RL) capabilities. By carefully designing each piece (policy init, reward, search, and learning) to be model-agnostic, you enable maximum flexibility.

In other words, it really can be a universal blueprint:

> Plug in your base model → define your reward → pick your search method → (optionally) do RL → deploy.
> 

This modular approach is precisely why you can imagine a “Reasoner as a Service,” where new models can be dropped in, get stronger reasoning, and self-improve over time


---
File: /sub-pages/Service Breakdown.md
---

# Service Breakdown

Below is a concise “service breakdown,” describing how each major component (or “service”) in the Reasoner Framework will specialize in a distinct aspect of building advanced reasoning capabilities. Together, they enable a modular plug-and-play system for transforming any LLM into a powerful reasoner.

---

## **1. Policy Initialization Service**

**Specialization:**

- *Starting point for a coherent, human-like reasoning policy.*
- *Equips* a baseline LLM with the fundamental ability to follow instructions, reason step by step, self-reflect, and check correctness at least at a basic level.

**Key Responsibilities:**

1. **Instruction Fine-Tuning**
    - Applies large, open instruction datasets (FLAN, Alpaca, etc.) to teach the model to follow user prompts and produce structured, helpful answers.
2. **Chain-of-Thought or Reasoning Behaviors**
    - Optionally refines the model on curated chain-of-thought data or uses prompt-based methods to activate reflection, decomposition, or self-check behaviors.
3. **Domain Specialization** (Optional)
    - If needed, fine-tunes or pre-trains on domain-specific corpora (code, math, medical data) so that the LLM is proficient in the tasks that follow.

**Deliverables:**

- A strong “initial policy” model (Checkpoint + Inference API) that can be used in subsequent reward, search, or RL pipelines.

---

## **2. Reward Design Service**

**Specialization:**

- *Generates or provides reward signals*—numerical or preference-based—to guide the model toward correct or aligned behavior.

**Key Responsibilities:**

1. **Outcome Reward**
    - Determines correctness purely from the *final* model output. Examples include code execution results or checking math solutions against known answers.
2. **Process Reward**
    - Scores *intermediate steps* (e.g., verifying partial solutions in math, code, or multi-turn problem-solving) to offer denser feedback.
3. **Preference-Based Reward (RLHF)**
    - Creates a “preference model” that ranks multiple solutions to the same query.
    - May be trained from human-labeled preference data or from a previously established “best-of-N” approach.
4. **Heuristics & World Knowledge** (Optional)
    - For specialized tasks, can incorporate domain heuristics (like style guidelines, factual checks, or safety constraints).

**Deliverables:**

- A “Reward API” callable by the Search or Learning services to (1) evaluate final solutions, or (2) provide partial feedback (step-level or preference-based).

---

## **3. Search / Inference Wrapper**

**Specialization:**

- *Scales up “thinking”* at inference or training time by generating multiple solutions or refining a single solution iteratively.

**Key Responsibilities:**

1. **Best-of-N (BoN) Sampling**
    - Independently samples multiple candidate answers, queries the Reward Design service to pick the best.
2. **Beam Search / Tree Search**
    - Systematically expands partial solutions, pruning suboptimal branches. May combine with a “value model” or other heuristics from Reward service.
3. **Sequential Revision (“Self-Refine”)**
    - Takes an initial draft from the LLM, runs a self-evaluation or environment check, and asks the LLM to revise. Repeats until a stopping criterion is met.
4. **MCTS (Monte Carlo Tree Search)** (Optional)
    - More advanced searching that can look ahead multiple steps using rollouts or partial expansions. Often used for math or code tasks where correctness is robustly checkable.

**Deliverables:**

- A “Search Service” that can orchestrate multi-pass generation and final selection, returning the best or a set of candidate solutions for further training.

---

## **4. Learning / Reinforcement Service**

**Specialization:**

- *Updates or fine-tunes the underlying LLM* using data produced by the Search and Reward services, aiming to improve the policy automatically.

**Key Responsibilities:**

1. **Behavior Cloning**
    - Filters out the top (highest-reward) solutions from Search, then performs supervised fine-tuning on these “expert demonstrations.”
2. **Policy Gradient (PPO, DPO, etc.)**
    - Learns from *all* candidate solutions, weighting them by reward, thus more effectively utilizing negative examples.
3. **Iterative Improvement** (AlphaGo-like)
    - Continuously alternates between (a) generating new data from the updated policy using the Search service, (b) evaluating it with the Reward service, and (c) updating the policy again.
4. **Reference Model and Baselines** (Optional)
    - Maintains reference or baseline models for stability, if needed (as in PPO’s “reference policy”).

**Deliverables:**

- An updated policy model that outperforms its earlier version by matching or exceeding the best solutions discovered via search and guided by reward signals.

---

## **Putting It All Together**

Each service exposes a clear interface:

1. **Policy Initialization** provides the base model (“Init Policy”).
2. **Reward Design** evaluates solutions or partial steps, returning numeric or preference-based scores.
3. **Search** runs extended inference (like Best-of-N, beam, MCTS, or iterative refinement) to generate high-reward solutions or to decide on a final best solution.
4. **Learning** consumes the data from Search+Reward, improving the policy’s parameters so that fewer or simpler search steps might be needed over time, or so that the model’s raw pass@1 accuracy increases.

By cleanly separating responsibilities, you can replace or upgrade each service (e.g., swap out beam search for MCTS, or add a better preference model) without breaking the rest of the system. This modular design directly follows the insights of the “Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective,” enabling robust, iterative improvement for any LLM plugged into the framework.


---
File: /Reasoning Framework: Building an Open, Modular System for Advanced LLM Reasoning.md
---

# Reasoning Framework: Building an Open, Modular System for Advanced LLM Reasoning

### **Inspiration**

This project draws on the “Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective,” - https://arxiv.org/pdf/2412.14135  which lays out a blueprint for creating powerful reasoning models by combining four components:

1. **Policy Initialization**
2. **Reward Design**
3. **Search**
4. **Learning**

By following these concepts, we aim to create a flexible, service-based “Reasoner Framework,” into which *any* large language model (LLM) can be plugged, gaining enhanced reasoning, better alignment, and iterative self-improvement capabilities.

---

### **Motivation and Goals**

Modern LLMs (e.g., OpenAI o1, DeepSeek-R1, etc.) exhibit advanced reasoning strategies like self-reflection, task decomposition, alternative solution proposals, and outcome verification. However, reproducing these capabilities in an open-source setting or for custom models remains challenging.

This project’s goal is to:

- **Enable** any baseline LLM to be turned into a “reasoning specialist.”
- **Modularize** each step (policy init, reward, search, learning) so they can be mixed, matched, and improved separately.
- **Scale** both train-time and inference-time “thinking” (search) to solve difficult tasks (math, coding, reasoning, alignment).
- **Deliver** a user-facing system in which organizations can upload or attach their models, pick a reward method, pick a search algorithm, and watch the model’s performance improve iteratively.

---

### **Project Scope and Components**

1. **Policy Initialization Service**
    - Provide an initial LLM (or let the user supply one) with baseline reasoning abilities—potentially combining:
        - **Pre-training** or *domain pre-training* (e.g., code or math corpora).
        - **Instruction Fine-tuning** on open instruction sets (e.g., FLAN, Alpaca) plus chain-of-thought.
        - **Supervised “Reasoning Behavior” Fine-tuning**, so the model can do problem analysis, step-by-step decomposition, self-evaluation, and error correction.
2. **Reward Design Service**
    - Supply dense or outcome-based rewards for a variety of tasks. For instance:
        - **Outcome Reward**: code execution or final numeric correctness for math problems.
        - **Process Reward**: verifying intermediate steps or partial correctness.
        - **Preference-based Reward**: from human annotations (RLHF) or automated preference ranking.
    - This service can be swapped or upgraded per domain (e.g., a code environment vs. math-checking vs. story writing).
3. **Search/Inference Wrapper**
    - A “meta” agent that orchestrates multiple calls to the LLM, generating solution candidates and refining them.
    - Supports:
        - **Best-of-N sampling** or **Beam Search** (with or without partial checks).
        - **MCTS** or other tree search techniques for large, complex tasks.
        - **Sequential revision** / “Self-Refine” loops that let the LLM correct itself iteratively.
    - This can run at *train-time* to gather high-quality data, or at *test-time* to produce better final answers.
4. **Learning/RL Service**
    - Consumes data from the Search step and the Reward service, then updates the LLM policy.
    - Allows either:
        - **Behavior Cloning** (supervised fine-tuning on high-reward solutions).
        - **Policy Gradient** (e.g., PPO or DPO) using both positive and negative solutions.
    - Over time, the model’s policy distribution aligns more closely with high-reward actions.

---

### **Planned Outcomes**

- **Reasoner API**
    
    An integrated pipeline where the user can:
    
    1. **Plug in a model**
    2. **Configure a reward** (or choose from existing ones)
    3. **Select a search strategy** (Best-of-N, MCTS, or iterative revision)
    4. **Optional RL fine-tuning**
    5. Obtain a “reasoning-augmented” LLM that can solve more complex tasks and keep improving via the same framework.
- **Evaluation Benchmarks**
    - Public math sets (e.g., MATH, GSM8K)
    - Code tasks (HumanEval, MBPP, etc.)
    - Possibly alignment tasks (preference-based)These will show how search + RL can systematically boost correctness and reasoning depth.
- **Iterative Improvement**
    
    Because each service is modular, new techniques (like a better process-reward, or a more efficient MCTS) can be dropped in without breaking the rest of the system.
    

---

### **Conclusion**

By implementing a reasoner framework inspired by the “Scaling of Search and Learning: A Roadmap to Reproduce o1…” paper, we aim to democratize advanced reasoning capabilities for LLMs. The end result is a robust, open framework that unifies the four cornerstones—Policy Initialization, Reward Design, Search, and Learning—offering any baseline model a path to become an expert-level reasoner with iterative self-improvement.

[Service Breakdown](https://www.notion.so/Service-Breakdown-17bae58cfe0880958289e405391ed375?pvs=21)

[Reasoning Framework Viability](https://www.notion.so/Reasoning-Framework-Viability-17bae58cfe08804b93a9e8980f51560d?pvs=21)

[Multi-Phased Execution Plan (Reasoning Framework)](https://www.notion.so/Multi-Phased-Execution-Plan-Reasoning-Framework-17bae58cfe0880689231ec5adfdaf705?pvs=21)

[Reasoning Datasets](https://www.notion.so/Reasoning-Datasets-17bae58cfe0880fab908f17afcbeceed?pvs=21)

[How can we use existing reasoning models and where do they fit in the process](https://www.notion.so/How-can-we-use-existing-reasoning-models-and-where-do-they-fit-in-the-process-17bae58cfe08802c8c0bd9473f64be92?pvs=21)

[Paper to domain mapping](https://www.notion.so/Paper-to-domain-mapping-17bae58cfe088090a9a0c66e0b0d4b7b?pvs=21)



---
File: /use-cases/enterprise-ready-generative-ai-applications/apolo-documentation-chatbot.md
---

# Apolo Documentation Chatbot

The **Apolo Documentation Chatbot** enables users to query Apolo’s technical documentation seamlessly, providing quick and accurate answers. Here’s how we built it.

![](../.gitbook/assets/2.png)

### **Step 1:** Set Up the Apolo RAG Architecture

The first step involves preparing the data infrastructure to support efficient querying and response generation. Here's what we'll do:

1. **Define the data storage structure**: Create a PostgreSQL schema with vector extensions to store embeddings and enable full-text indexing for fast retrieval.
2. **Chunk the documentation**: Preprocess the Apolo documentation into manageable text chunks for embeddings and efficient retrieval.
3. **Generate embeddings**: Use an embedding LLM to convert text chunks into numerical representations for semantic search.
4. **Ingest data into PostgreSQL**: Store the processed chunks and their embeddings in the database for future queries.

Here’s how we implemented this:

```python
def build_apolo_docs_rag():
    table_name = "apolo_docs"
    chunk_size = 1024
    chunk_overlap = 100

    print("1. Processing data")
    apolo_docs_path = clone_repo_to_tmp(
        repo_url="https://github.com/neuro-inc/platform-docs.git"
    )
    markdown_files = glob.glob(os.path.join(apolo_docs_path, "**/*.md"), recursive=True)
    docs = list(
        chain.from_iterable(
            [UnstructuredMarkdownLoader(f).load() for f in markdown_files]
        )
    )
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    ).split_documents(docs)

    print("2. Get ebeddings")
    sentences = [x.page_content for x in chunks]
    embeddings = get_embeddings(sentences=sentences)

    print("3. Ingest data")
    create_schema(table_name=table_name, dimensions=len(embeddings[0]))
    insert_data(
        table_name=table_name, embeddings=embeddings, sentences=sentences, batch_size=64
    )
```

**Breaking Down the Steps**

* **Processing Data**:\
  The `clone_repo_to_tmp()` function pulls the Apolo documentation repository, and the UnstructuredMarkdownLoader processes _`.md`_ files into raw text. The text is then chunked into overlapping segments using RecursiveCharacterTextSplitter, which ensures each chunk retains contextual relevance.
* **Generating Embeddings**:\
  To represent text chunks numerically, we use the `get_embeddings()` function. It leverages the embedding LLM hosted on Apolo’s platform to create vector representations for semantic search.

```python
def get_embeddings(sentences: List[str], batch_size: int = 4) -> List[List[float]]:
    embeddings = []
    embedding_client = get_embedding_client()
    for i in tqdm(range(0, len(sentences), batch_size)):
        sentences_batch = sentences[i : i + batch_size]
        response_batch = embedding_client.embeddings.create(
            input=sentences_batch, model="tgi"
        )
        embeddings.extend([x.embedding for x in response_batch.data])
    return embeddings
```

* **Ingesting Data**: The processed chunks and embeddings are stored in PostgreSQL. Using vector extensions (pgvector), we create a table with a schema that supports vector-based operations for semantic search.

```python
def create_schema(table_name: str, dimensions: int):
    conn = get_db_connection()

    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    conn.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

    register_vector(conn)

    conn.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.execute(
        f"CREATE TABLE {table_name} (id bigserial PRIMARY KEY, content text, embedding vector({dimensions}))"
    )
    conn.execute(
        f"CREATE INDEX ON {table_name} USING GIN (to_tsvector('english', content))"
    )
```

### **Step 2: Query the Apolo Documentation**

Once the RAG architecture is set up, the next step is enabling queries. The system retrieves relevant documentation chunks, generates a response using a generative LLM, and logs the interaction for continuous improvement.

Here’s the query flow:

1. **Retrieve relevant chunks**:
   * Use **semantic search** to find embeddings closest to the query embedding.
   * Use **keyword search** for matching phrases or terms in the text.
2. **Re-rank results**: Combine results from semantic and keyword searches and sort them by relevance using a reranker model.
3. **Generate the response**: Augment the top-ranked chunks with the user query to create a context-rich prompt for the generative LLM.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfw0XgUwdn-pmDddruh9IYidEa_vUQR-rACHlJ-4dOuxmABYO-PK74xPvJnkimV6rsncKs3Lg_EnWukLwBh8_ai1j4uLWEtLkBZQpkwAHc_UPLPDHuEe3j6FkaxZn5FFTEN1On46A?key=cAc3C7o7nPsQcNEZZEPwoSYs" alt=""><figcaption></figcaption></figure>

4. **Log results**: Store the query, context, and response in Argilla for feedback and future fine-tuning.

```python
def query_apolo_docs_rag(query: str = "How to run mlflow?"):
    table_name = "apolo_docs"
    print("1. Get query embedding.")
    query_embedding = get_embeddings(sentences=[query])[0]

    print("2. Run semantic search.")
    semantic_search_result = semantic_search(
        table_name=table_name, query_embedding=query_embedding, top_n=20
    )

    print("3. Run keyword search.")
    keyword_search_result = keyword_search(table_name=table_name, query=query, top_n=20)

    print("4. Rerank results.")
    search_result = rerank(
        query=query, sentences=semantic_search_result + keyword_search_result, top_n=5
    )

    print("5. Augment & generate.")
    context = "\n".join(search_result)
    response = generate_with_context(query=query, context=context)

    console = Console()
    console.print(Panel(response, title="Generated Response", border_style="green", style="bold green"))

    print("6. Save response.")
    log_sample(
        query=query,
        context=context,
        response=response,
        dataset_name=table_name,
        keyword_search="\n".join(keyword_search_result),
        semantic_search="\n".join(semantic_search_result),
    )
```

### **Step 3:** Continuous Improvement with Argilla

<figure><img src="../.gitbook/assets/4.png" alt=""><figcaption></figcaption></figure>

![](../.gitbook/assets/5.png)

![](../.gitbook/assets/6.png)

Feedback loops are critical for improving RAG applications. Using Argilla:

* Each query, context, and response is logged for evaluation.
* Users can rate the relevance of contexts and responses, enabling targeted fine-tuning of embeddings, search algorithms, or even the LLM itself.

```python
def log_sample(
    query: str,
    context: str,
    response: str,
    semantic_search: str,
    keyword_search: str,
    dataset_name: str,
):
    client = rg.Argilla(api_url=ARGILLA_URL, api_key="admin.apikey")

    dataset = client.datasets(name=dataset_name)
    if not dataset.exists():
        settings = rg.Settings(
            fields=[
                rg.TextField(name="query"),
                rg.TextField(name="response"),
                rg.TextField(name="context"),
                rg.TextField(name="semantic_search"),
                rg.TextField(name="keyword_search"),
                
            ],
            questions=[
                rg.RatingQuestion(
                    name="context_relevance",
                    title="Relevance of the context",
                    values=[1, 2, 3, 4, 5],
                ),
                rg.RatingQuestion(
                    name="response_relevance",
                    title="Relevance of the response",
                    values=[1, 2, 3, 4, 5],
                ),
            ],
        )
        dataset = rg.Dataset(
            name=dataset_name,
            settings=settings,
            workspace="admin",
            client=client,
        )
        dataset.create()

    record = rg.Record(
        fields={
            "query": query,
            "context": context,
            "response": response,
            "semantic_search": semantic_search,
            "keyword_search": keyword_search,
        }
    )

    dataset.records.log([record])

```



---
File: /use-cases/enterprise-ready-generative-ai-applications/canada-budget-rag.md
---

# Canada Budget RAG

![](../.gitbook/assets/7.png)

**Why Build a Canada Budget Chatbot?**

The Canada Budget chatbot is a prime example of how generative AI applications can simplify complex document querying. Here's why such a system is valuable:

* **Accessibility**: Users can quickly obtain answers to specific budget-related queries without navigating lengthy documents.
* **Efficiency**: Retrieval-based search ensures responses are not only accurate but also highly relevant.
* **Customization**: By using domain-specific data (Canada Budget documents), the chatbot delivers tailored insights unavailable in generic models.

RAG isn't limited to small datasets. Here’s how Apolo processes the 500+ pages of Canada's 2024 Budget to allow for instant querying.

### **Step 1:** Set Up the Canada Budget RAG Architecture

Similar to the Apolo Documentation chatbot, this use case starts by preparing the data pipeline for effective querying. The process includes:

1. **Defining the data storage structure**: Create a PostgreSQL schema optimized for storing and retrieving text embeddings.
2. **Processing the Canada Budget**: Extract text from PDF files and chunk them for efficient indexing.
3. **Generating embeddings**: Convert the text chunks into vector embeddings for semantic search.
4. **Ingesting data into PostgreSQL**: Store processed data and embeddings in the database for querying.

```python
def build_canada_budget_rag():
    table_name = "canada_budget"
    chunk_size = 1024
    chunk_overlap = 100
    data_path = "./data/canada/"

    pdf_files = list(Path(data_path).iterdir())

    print("1. Processing data")
    list_of_pages = [
        PyPDFLoader(pdf_files[idx]).load() for idx in range(len(pdf_files))
    ]
    docs = list(chain.from_iterable(list_of_pages))
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    ).split_documents(docs)

    print("2. Get ebeddings")
    sentences = [x.page_content for x in chunks]
    embeddings = get_embeddings(sentences=sentences, batch_size=32)

    print("3. Ingest data")
    create_schema(table_name=table_name, dimensions=len(embeddings[0]))
    insert_data(
        table_name=table_name, embeddings=embeddings, sentences=sentences, batch_size=64
    )
```

**Breaking Down the Steps**

* **Processing Data**:\
  Using PyPDFLoader, we extract text from budget documents in PDF format. This raw text is then chunked into overlapping segments for embeddings and retrieval. This ensures each chunk remains contextually relevant during queries.
* **Generating Embeddings**:\
  The text chunks are passed through the `get_embeddings()` function, leveraging an embedding LLM hosted on Apolo to produce semantic representations.
* **Ingesting Data**:\
  The processed data and embeddings are ingested into PostgreSQL using a custom schema. This schema supports vector-based queries for semantic search and text indexing for keyword-based search.

### **Step 2:** Query the Canada Budget Chatbot

Once the architecture is in place, the next step is to enable queries on the Canada Budget dataset. The query flow follows a similar structure to the Apolo Documentation chatbot:

1. **Retrieve relevant chunks**:
   * Perform **semantic search** to find embeddings most relevant to the query.
   * Conduct **keyword search** for exact or approximate term matches.
2. **Re-rank results**: Combine results from both search methods and rank them by relevance using a reranker model.
3. **Generate the response**: Feed the top-ranked chunks into a generative LLM along with the query for contextually accurate responses.
4. **Log results**: Store the query, context, and response in Argilla for evaluation and iterative improvement.

```python
def query_canada_budget_rag(query="What actions is the government taking to increase the new housing supply?"):
    table_name = "canada_budget"

    print("1. Get query embedding.")
    query_embedding = get_embeddings(sentences=[query])[0]

    print("2. Run semantic search.")
    semantic_search_result = semantic_search(
        table_name=table_name, query_embedding=query_embedding, top_n=20
    )
    print("3. Run keyword search.")
    keyword_search_result = keyword_search(table_name=table_name, query=query, top_n=20)

    print("4. Rerank results.")
    search_result = rerank(
        query=query, sentences=semantic_search_result + keyword_search_result, top_n=5
    )

    print("5. Augment & generate.")
    context = "\n".join([doc for doc in search_result])
    response = generate_with_context(query=query, context=context)

    console = Console()
    console.print(Panel(response, title="Generated Response", border_style="green", style="bold green"))

    print("6. Save response.")
    log_sample(
        query=query,
        context=context,
        response=response,
        dataset_name=table_name,
        keyword_search="\n".join(keyword_search_result),
        semantic_search="\n".join(semantic_search_result),
    )
```

### **Step 3:** Feedback and Iterative Improvement

Feedback plays a vital role in refining the chatbot’s performance over time. The Canada Budget chatbot also utilizes the **Argilla-powered feedback loop** described in the previous case.&#x20;

Users can:

* Rate the relevance of contexts and responses.
* Identify areas for improvement in chunking, embedding quality, or retrieval mechanisms.

![](../.gitbook/assets/8.png)

![](../.gitbook/assets/9.png)



---
File: /use-cases/generic/ml-model-lifecycle-on-apolo-platform/end-to-end-ml-model-lifecycle-using-apolo-cli.md
---

# End-to-End ML Model Lifecycle using Apolo CLI

This guide demonstrates how to manage a complete machine learning workflow on the Apolo platform, from environment setup to model deployment. We'll walk through the entire ML lifecycle using **Apolo Flow**, a powerful declarative workflow system ([full documentation here](https://docs.apolo.us/index/apolo-flow-reference)). While this guide uses the command-line interface (CLI), these operations can also be performed through the Apolo Console GUI for those who prefer a graphical experience using our built-in Apps such as Jupyter, MLFlow and Apolo Jobs.

We'll use a modified version of PyTorch's "Name Classification using RNN" example (originally from [PyTorch's tutorials](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)) to showcase how Apolo Flow simplifies the ML lifecycle management.

### Prerequisites

* Apolo CLI tools
* Access to an Apolo platform instance
* Basic understanding of ML workflows

### Understanding Apolo Flow

Apolo Flow is a declarative workflow system that allows you to define your entire ML infrastructure as code. The `.apolo/live.yml` file in this example is a Flow configuration that defines:

1. Container images for both training and serving
2. Storage volumes for data, code, and models
3. Jobs for training, serving, and monitoring
4. Dependencies between components

By using this declarative approach, you can ensure reproducibility and easily share workflows with team members. While we'll use the CLI in this guide, all these operations can also be performed through the Apolo Console GUI.

### Step 1: Clone the Example Repository

Start by cloning the example repository that contains all the necessary code and configuration:

```bash
# Clone the model lifecycle example repository
git clone https://github.com/neuro-inc/model-lifecyle-example
cd model-lifecyle-example
```

The repository contains:

* `.apolo/live.yml` - Workflow definition file
* `scripts/` - Training and serving code
* `scripts/Dockerfile` - Container definition for training
* `scripts/Dockerfile.server` - Container definition for serving

#### Important Note About Compute Presets

Before proceeding, review the `live.yml` file and pay attention to the `preset` fields for both building images and running jobs. These presets define the computational resources allocated (CPU, RAM, GPU) and might have different names in your specific Apolo cluster.

```yaml
# Example preset definitions in live.yml
images:
  train:
    build_preset: cpu-large  # This preset name may differ in your cluster
    
jobs:
  train:
    preset: cpu-large  # This preset name may differ in your cluster
```

To find the correct preset names for your cluster:

1. Navigate to your Apolo Console
2.  Go to Cluster > Settings > Resources



    <figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
3. Note the available preset names
4. Modify the relevant fields in your `live.yml` file accordingly

Using the correct preset names will ensure your jobs have the appropriate resources and can run successfully in your environment.

### Step 2: Setup Environment

Ensure you have the Apolo CLI tools installed:

```bash
# Install pipx if not already available (manages Python applications)
pip install -U pipx

# Install the complete Apolo toolkit with isolated dependencies
pipx install apolo-all
```

### Step 3: Authentication and Resource Preparation

Log in to your Apolo platform instance:

```bash
# Log in to your organization's Apolo instance
# For custom clusters, specify the URL after the command:
# apolo login https://api.apolo.yourcompany.ai/api/v1
apolo login

# Create a persistent 2GB disk for MLflow's backend storage (if not already done)
# This ensures experiment tracking data persists across sessions
apolo disk create 2GB --name global-mlflow-db
```

### Step 4: Launch MLflow Tracking Server

Start the MLflow service to track your experiments, parameters, metrics, and artifacts:

```bash
# Start the MLflow tracking server using the configuration from live.yml
# This will output a URL where you can access the MLflow UI
apolo-flow run mlflow
```

The MLflow server provides:

* A web UI for experiment comparison
* Metadata storage for runs
* Artifact storage for models and other outputs
* A REST API for logging from your training jobs

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption><p>MLFlow interface displaying a list of experiments</p></figcaption></figure>

### Step 5: Prepare Training Data

Download and prepare the training data:

```bash
# Create data directory and download sample dataset
mkdir -p data && curl https://download.pytorch.org/tutorial/data.zip -o data/data.zip
unzip data/data.zip -d data/names && rm data/data.zip
```

> **Important Note About Data and Code Management**:
>
> The Apolo platform automatically synchronizes local directories with remote storage when you use the `local` parameter in the `volumes` section of the `live.yml` file. This means you don't need to manually copy code or data files to the container during build time. When you run a job, Apolo will ensure all the local files defined in your volumes are available in the container at the specified mount points.
>
> For example, in our `live.yml`, we defined:
>
> ```yaml
> volumes:
>   data:
>     remote: storage:/$[[ project.project_name ]]/$[[ flow.project_id ]]/data
>     mount: /project/data
>     local: data/names
> ```
>
> This automatically syncs the contents of your local `data/names` directory to the remote storage, which is then mounted at `/project/data` in the container.

### Step 6: Build Training Environment

Build the Docker image that contains all dependencies for training:

```bash
# Build the training image defined in the live.yml file
# This uses the Dockerfile at scripts/Dockerfile 
apolo-flow build train
```

The training image includes:

* Python environment
* PyTorch framework
* Custom code dependencies for the RNN name classifier

### Step 7: Train the Model

Launch the training job which will:

* Use the data volume mounted at `/project/data`
* Save the model to the models volume
* Log metrics and parameters to MLflow

```bash
# Run the training job defined in live.yml
# This executes train.py with the configured volumes and environment
apolo-flow run train
```

During training, you can:

* Monitor progress in the MLflow UI
* Access logs via `apolo-flow logs train`

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption><p>Average Loss metric decrease displayed in MLFlow</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Model training artifacts such as the weights file and metadata files displayed on MLFlow</p></figcaption></figure>

### Step 8: Deploy Model Serving API

Deploy the trained model as a RESTful API service:

```bash
# First build the serving image with the serving dependencies
apolo-flow build serve

# Launch the model serving API
apolo-flow run serve
```

The serving job:

* Loads the model from the shared models volume
* Exposes a FastAPI endpoint for predictions
* Provides Swagger documentation at the `/docs` endpoint
* Can be scaled or updated independently of training

#### Accessing Your Deployed Model API

After running `apolo-flow run serve`, you'll see output in your terminal with details about the deployed service. Look for the "Http Url" in the output—this is the address where your model API is now available.

When you open this URL in your browser, you'll see a simple "service is up" message, confirming that the API is running successfully.

To interact with your model, add `/docs` to the end of the URL. This will take you to an automatically generated API documentation interface powered by FastAPI and Swagger UI. Here, you can:

1. See all available endpoints (in this example, the `/predict` endpoint)
2. Test the model directly from your browser by clicking on the endpoint
3. Expand the endpoint details, click "Try it out", and provide a sample input
4. Execute the request and view the model's predictions

For example, you can submit a name like "Patrick" along with the number of predictions you want, and the model will return the most likely country origins for that name based on its training.

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

### Additional Workflows

The configuration also supports:

```bash
# Launch a Jupyter notebook server for interactive development
apolo-flow run jupyter
```

### Monitoring and Management

```bash
# List all running jobs
apolo ps

# View logs from a specific job
apolo-flow logs serve

# Stop a running job
apolo kill serve
```

This workflow demonstrates the power of declarative ML pipelines on Apolo, enabling reproducible, scalable, and production-ready machine learning workflows. The RNN name classifier example shows how even sophisticated deep learning models can be easily trained and deployed using the platform's orchestration capabilities.




---
File: /use-cases/generic/ml-model-lifecycle-on-apolo-platform/ml-model-lifecycle-using-apolo-console.md
---

# ML Model Lifecycle using Apolo Console

This comprehensive guide will walk you through creating a complete machine learning workflow using Apolo's platform. You'll learn how to:

* Set up a Jupyter Lab environment for model development
* Train a simple classification model with scikit-learn
* Track experiments and models with MLflow
* Convert models to ONNX format for deployment
* Deploy your model as an inference service using NVIDIA Triton

### Prerequisites

* Basic familiarity with Python and machine learning concepts

### 1. Accessing the Apolo Console

1. Log in to the [Apolo](https://app.gitbook.com/o/-MMLX64i1AQdS3ehf2Kg/s/UD8kiAsnN8MKP7nzsJRQ/)
2. Verify your project selection in the top-right corner dropdown

### 2. Setting Up Your Jupyter Lab Environment

1. Navigate to the **Apps** section in the left sidebar, make sure you have the **All Apps** tab selected to view available applications
2. Locate and click on the **Jupyter Lab** card
3.  Click the **Install** button

    <figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>
4.  Configure your Jupyter Lab instance:

    * Under **Resources**, select a preset (we'll use `cpu-small` for this tutorial)
    * Under **Metadata**, name your instance (e.g., `jupyter-lab-demo`)
    * Click **Install App**

    <figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>
5.  Wait for the status to change from **Pending** to **Succeeded**

    <figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

Find more about launching Jupyter in Apolo by going to our [Jupyter Notebook page](https://app.gitbook.com/s/UD8kiAsnN8MKP7nzsJRQ/apolo-console/apps/available-apps/jupyter-notebook).&#x20;

### 3. Setting Up MLflow for Experiment Tracking

1. Return to the Apolo Console
2. Navigate to **Apps** > **All Apps**
3.  Find and install the **MLflow** application:

    * Select a resource preset (e.g., `cpu-small`)
    * Name your instance (e.g., `mlflow-demo`)
    * Click **Install App**

    <div><figure><img src="../../.gitbook/assets/image (55).png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure></div>
4. Wait for the MLflow instance to reach the **Succeeded** state

### 4. Setting Up Your Development Environment

1. Return to **Apps** > **Installed Apps** and find your Jupyter Lab instance
2.  Click the **Open** button to launch Jupyter Lab in a new tab

    <figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>
3.  Open a terminal by clicking **Terminal** under the "Other" section in the launcher

    <figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>
4.  Navigate to the persistent storage location:

    ```bash
    cd /var/storage
    ```
5.  Clone the example repository:

    ```bash
    git clone https://github.com/neuro-inc/model-lifecycle-example
    ```

### 5. Training Your Machine Learning Model

1.  Navigate to the cloned repository through the file browser:

    * Open the `model-lifecycle-example` directory
    * Open the `notebooks` directory
    * Open `training-demo.ipynb`

    <figure><img src="../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>
2. Run the notebook cells sequentially (using Shift+Enter or the Run button)

### 6. Reviewing Your Model in MLflow

1. Return to the Apolo Console
2. Navigate to **Apps** > **Installed Apps**
3. Find your MLflow instance and click **Open**
4.  Explore the experiment run:

    * Click on the most recent run
    * Review the logged parameters, metrics, and artifacts

    <figure><img src="../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>
5.  Promote your ONNX model to production:

    * Click on the **Models** tab in the MLflow UI
    * Select the `onnx_iris_perceptron` model
    * Click on the latest version
    * **Important:** Ensure the **New model registry UI** toggle is turned off

    <figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

    * Change the **Stage** from "None" to "Production"
    * Confirm the stage transition

    <figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

### 7. Deploying Your Model with Apolo Deploy

1. Return to the Apolo Console
2. Navigate to **Apps** > **All Apps**
3.  Find and install **Apolo Deploy**:

    * Select a resource preset (e.g., `cpu-small`)
    * Under **Integrations**, select your MLflow instance
    * Name your deployment (e.g., `apolo-deploy-demo`)
    * Click **Install App**

    <figure><img src="../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>
4. Wait for Apolo Deploy to reach the **Running** state
5.  Open Apolo Deploy and configure your model deployment:

    * Locate the `onnx_iris_perceptron` model in Production stage
    * Click the dropdown in the **Deployment** column
    * Configure the deployment:
      * Set **Server type** to `Triton`
      * Set **Create new server instance** to `True`
      * Set an optional server name (default: `triton`)
      * Select a resource preset
      * Set **Force Platform Auth** to `False` (for demo purposes only)
    * Click **Deploy**

    <div><figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure></div>
6.  Wait for the deployment to complete

    <figure><img src="../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

### 8. Testing Your Deployed Model

1. Return to your Jupyter Lab application
2. Open the notebook called `inference-demo.ipynb`
3. Run the cells to test your deployed model

<figure><img src="../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

### Conclusion

Congratulations! You've successfully:

* Set up a Jupyter Lab environment on Apolo
* Trained a simple classification model
* Tracked your experiment and model with MLflow
* Converted your model to ONNX format
* Deployed your model using NVIDIA Triton via Apolo Deploy
* Tested your deployed model endpoint

This workflow demonstrates a complete MLOps pipeline that you can adapt for your own machine learning projects.

### Additional Resources

* [Apolo Documentation](https://docs.apolo.us/)
* [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
* [NVIDIA Triton Inference Server](https://developer.nvidia.com/nvidia-triton-inference-server)
* [ONNX Model Format](https://onnx.ai/)



---
File: /use-cases/generic/ml-model-lifecycle-on-apolo-platform/README.md
---

# ML Model Lifecycle on Apolo Platform




---
File: /use-cases/image-and-video-processing/howto-lora-models-with-stable-diffusion.md
---

# HOWTO: Lora models with Stable Diffusion

### What is LoRA (Low-Rank Adaptation)?

**LoRA**, short for **Low-Rank Adaptation**, is a technique used to **fine-tune large AI models** (like language or vision models) **efficiently and with fewer resources**.

Instead of updating all the parameters in a massive pre-trained model—which is expensive and memory-intensive—LoRA freezes the original model and **adds small, trainable layers** (called _low-rank matrices_) to specific parts of the model (like attention layers). These additions learn the task-specific changes, allowing the core model to remain unchanged.

Using **LoRA models with Stable Diffusion** is a super popular way to customize the style, character, or theme of your image generations without retraining the whole model.

### How to Use LoRA in Apolo platform with Stable Diffusion

Prerequisites:

* Install Apolo cli using [this](https://docs.apolo.us/index/apolo-concepts-cli/installing) doc
* Clone [this](https://github.com/neuro-inc/sdnext) repo

#### Add secret value with personal Hugging Face Token&#x20;

```
apolo secret add HF_TOKEN <your_token>
```

**Run Stable Diffusion job, replacing the secret value, preset, and any other configuration**

```
apolo-flow run stablediffusion
```

**Download the model using SDnext interface**

Go to Models -> HuggingFace

<figure><img src="../.gitbook/assets/image (29).png" alt=""><figcaption><p>HuggingFace model download interface</p></figcaption></figure>

Generate the first image:

**Prompt:**

Ghibli style futuristic stormtrooper with glossy white armor and a sleek helmet, standing heroically on a lush alien planet, vibrant flowers blooming around, soft sunlight illuminating the scene, a gentle breeze rustling the leaves

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

### Lora model

Let's find a trained model on Civit.ai, we need to filter model by our Stable Diffusion version.

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption><p>Civit.AI search models interface</p></figcaption></figure>

Alternative can be HuggingFace search. (tags: Lora, Stable Diffusion, 3.5)

I will use "[studio-ghibli-style-lora](https://huggingface.co/alvarobartt/ghibli-characters-sd3.5-lora)" Lora model.

Now we need to copy our model into the /Lora directory of our storage volume

```
apolo cp -r studio-ghibli-style-lora.safetensors storage:sdnext/models/Lora/studio-ghibli-style-lora.safetensors
```

After Model Copying, and hitting the refresh button on the Lora tab, we should be able to see our model downloaded.

Click on your Networks -> Lora tab, hit refresh, and click on your Lora model, that will add Lora to youre prompt, and you will be able to generate images using it.

For example we generated ghibli-style stormtrooper.

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption><p>Ghibli style stormtrooper</p></figcaption></figure>

### References:

* [Apolo cli](https://docs.apolo.us/index/apolo-concepts-cli/installing)
* [SDnext repository](https://github.com/neuro-inc/sdnext)
* [Apolo secrets cli documentation](https://docs.apolo.us/index/apolo-cli/commands/secret)
* [Civit AI model storage](https://civitai.com/)






---
File: /use-cases/image-and-video-processing/synthetic-data-generation-using-stable-diffusion.md
---

# Synthetic Data Generation using Stable Diffusion

The example shows how to run [Stable Diffusion](https://huggingface.co/stabilityai/stable-diffusion-3-medium) model via Apolo platform and generate images for your synthetic dataset.&#x20;

### Synthetic data

Synthetic image data refers to **computer-generated visuals** that simulate real-world scenes, rather than capturing them from physical environments. Unlike traditional photographs, synthetic images do not depict a real-world moment in time but are designed based on real-world concepts. They retain the **semantic essence** of objects such as cars, tables, or houses, making them valuable for **computer vision applications**.

In essence synthetic images are pictures generated using computer graphics, simulation methods and artificial intelligence (AI), to represent reality with high fidelity.

There are plenty of applications of synthetic data in modern computer vision pipelines.

#### Why to use synthetic data in your dataset:

* **Expands Variability**: AI-generated images introduce **variations in lighting, angles, and environments** that may be missing in real-world datasets.
* **Reducing Bias**: If a dataset lacks diversity (e.g., images of cars mostly in daylight), synthetic data can **balance** the distribution by adding night-time, foggy, or rainy conditions.
* **Enhances Generalization**: Helps models perform better in **unseen scenarios** by providing edge cases not commonly found in real-world data.

### Generating images using Apolo

The example show HOWTO run [Stable Diffusion 3](https://huggingface.co/stabilityai/stable-diffusion-3-medium/tree/main) using WebUI, Cli, and API.

#### Step1: Deploy Stable Diffusion using Apolo app

[Log in](https://console.apolo.us/auth) to your Apolo account

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption><p>Login screen</p></figcaption></figure>

Find Stable Diffusion in your Apps tab

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption><p>Apps tab</p></figcaption></figure>

Deploy Stable Diffusion version, if you want to minimize the size, specify only weights

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption><p>Stable Diffusion installation Tab</p></figcaption></figure>

Now, check your App url at the details -> Outputs

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

#### Use-case:&#x20;

Stable Diffusion is often used to generate imaginative and playful images, such as a penguin skateboarding through a neon city or a cat wearing a top hat, sipping tea in a Victorian parlor. While these highlight its creative potential, this demo focuses on showcasing its practical applications for real-world business use cases, demonstrating how it can drive impactful solutions across various industries.

Imagine you're developing an **instance segmentation or object detection model** specifically for identifying and segmenting different rooms inside a house or detecting objects in the . While you already have some 2D drawings to work with, the dataset is insufficient for training an effective model. To address this limitation, generating synthetic data could be a valuable solution, helping to supplement your existing dataset and improve the model's performance by providing diverse and varied examples for training.

So by the time you have

* Lack of Real-World Data for 2d drawings.
* Data Collection is not possible.

Here synthetic data can be handy.

**We will simply define a prompt** \
Simple 2D architectural floorplan with clean, black lines on a white background. The layout should include walls, rooms, and basic features like doors and windows, all drawn with clear black lines. The floorplan should be minimalistic and easy to understand, resembling the style of technical drawings or blueprints.

**Also, it is very important to define a negative prompt**\
colors, textures, shading, and any 3D elements. furniture, patterns, or decorative designs. Exclude any details like landscapes, people, or non-architectural elements. Keep the drawing simple, with just black lines and a white background. Round shapes\


Generated example:

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption><p>Generated Floorplan</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption><p>Some of the generated images.</p></figcaption></figure>

We can tune the prompt further, so it does not make blurry lines, and fits our needs for the detection/segmentation model.

Now Check the API&#x20;

```bash
<APP_URL>/sdapi/v1/txt2img
```

Now you can run the script and review manually the generated images.

You can adjust image size, batch\_number, steps, see [https://vladmandic.github.io/sdnext-docs/](https://vladmandic.github.io/sdnext-docs/)

Swagger documentation for the text2img parameters is here:\
\<APP\_URL>/docs

```
import requests
import base64
from PIL import Image
from io import BytesIO

# Define the URL for the API
url = "<APP_URL>/sdapi/v1/txt2img"

# Define the headers
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Define the base data template
base_req_body = {
    "prompt": "Simple 2D architectural floorplan with clean, black lines on a white background. The layout should include walls, rooms, and basic features like doors and windows, all drawn with clear black lines. The floorplan should be minimalistic and easy to understand, resembling the style of technical drawings or blueprints. ",
    "negative_prompt": "colors, textures, shading, and any 3D elements. furniture, patterns, or decorative designs. Exclude any details like landscapes, people, or non-architectural elements. Keep the drawing simple, with just black lines and a white background. Round shapes",
    "batch_size": 1,
    "steps": 20
}


# Function to send request and parse base64 image response
def generate_and_parse_image(loop_number):
    # Send the POST request to the API
    response = requests.post(url, json=base_req_body, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Assuming the response contains a base64-encoded image string
        response_json = response.json()
        images = response_json.get('images')  # 'image' is the key for base64 string

        if images:
            for img_batch_num, image in enumerate(images):
                # Decode the base64 string to bytes
                image_data = base64.b64decode(image)

                # Convert the byte data to an image
                image = Image.open(BytesIO(image_data))

                # Construct the file name
                filename = f"loop_{loop_number}_img_batch_{img_batch_num}.png"

                # Save the image to a file
                image.save(filename)
                print(f"Image saved as '{filename}'")
    else:
        print(
            f"Request failed for loop {loop_number}, with status code {response.status_code}: {response.text}")


if __name__ == '__main__':

    # Loop for 10 iterations
    for i in range(1, 11):
        # Generate the image and save it
        generate_and_parse_image(i)

```

### References

* [SDNext repository](https://github.com/neuro-inc/sdnext)
* [Stability AI](https://stability.ai/) website
* [Stability AI HuggingFace](https://huggingface.co/stabilityai)
* [Stable Diffusion prompt guide](https://stability.ai/learning-hub/stable-diffusion-3-5-prompt-guide)




---
File: /use-cases/llms/autonomous-research-with-agentlaboratory-deepseek-r1-vs.-openai-o1.md
---

---
description: >-
  This is a multi part series on Autonomous Research with leading Large Language
  Models.
---

# Autonomous Research with AgentLaboratory: DeepSeek R1 vs. OpenAI o1

This report examines the output of two distinct autonomous research setups— around **DeepSeek R1** and **OpenAI o1**—produced with AgentLaboratory. Both results aim to demonstrate multi-phase reasoning pipelines for code and math tasks, incorporating key components such as **policy initialization**, **reward design**, **search**, and **learning**. \
\
These tests were conducted in a fully autonomous manner, and the same prompt was provided for each of the models. You may find the full prompt here:

{% code overflow="wrap" %}
```
python ai_lab_repo.py --api-key "<provide_api_key>" --llm-backend "<pick model deepseek-chat/o1>" --research-topic "I need you to implement the Reasoning Framework discussed in these docs '{FILE}' as a cli tool, implement scripts for dataset creation based on all 4 services, kind of like what will be collected during working services, so we can continue the improvement loop. For starter we can start on the Open Reasoner dataset and work our way from there. I need those 4 services implemented and a paper presenting the idea. Don't waste too much time on one approach, do it thoroughly but keep it only as long as needed. Be strategic on the things you incorporate like a reducer that keeps adding to the main state continuously developing and refining the approach but in a counscious way so you don't overthink it. Write all the code and output the paper in the research_dir at the root of this project" --file-path "./projects/Reasoning_Framework.md"
```
{% endcode %}

I've attached the `Reasoning_Framework.md` where I provide more details of how I would want this problem approached and implemented:&#x20;

* How can we use existing reasoning models, and where do they fit in the process
* Multi-phased execution plan
* Paper to domain mapping
* Reasoning datasets
* Reasoning framework viability
* Service Breakdown
* Main project description

We forked the AgentLaboratory [here](https://github.com/neuro-inc/AgentLaboratory), where we added support for file injection in prompt, among other fixes.\
\
In short, the Reasoning Framework is a **modular, service-based framework** that any organization can use to turn a baseline LLM into a more advanced “reasoning” model. It breaks the system into four key services—**Policy Initialization**, **Reward Design**, **Search**, and **Learning**—each handled by its own module. The goal is to let users:

1. **Attach or initialize a model** (e.g., via instruction-tuning).
2. **Define a reward function** (code execution checks, human preferences, etc.).
3. **Run a search or iterative refinement** to generate better solutions.
4. **Optionally apply RL or distillation** to improve the model.

Together, these steps form a **multi-phased pipeline** (from basic setup and data handling through final deployment) that guides the implementation of a robust “reasoner” capable of self-correction, task decomposition, and iterative improvement. The directories each detail a different aspect of the framework—datasets, references, execution plan, service breakdown, distillation, reinforcement-learning, and integration points for existing reasoning models—so you can mix, match, or upgrade components without reworking the entire system.

{% file src="../.gitbook/assets/Reasoning_Framework.md" %}

As you can see, this was no easy task for these models, this agentive system and proved very challenging to humans as well, it should work better on simpler tasks with human in the loop.

You can try this yourself by deploying R1 variants on Apolo and cloning the AgentLaboratory repo:

* [DeepSeek R1 model deployment](https://docs.apolo.us/index/use-cases/llms/deepseek-r1-model-deployment)&#x20;
* [DeepSeek R1 distilled models deployment](https://docs.apolo.us/index/use-cases/llms/deepseek-r1-distilled-models)
* [AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) (official) or use the [fork](https://github.com/neuro-inc/AgentLaboratory) mentioned above

### Goal

In short the goal is to explore how we can create a reasoning framework given the provided information. Both DeepSeek R1 and OpenAI o1 aim to create the a form of a reasoning framework/pipeline depending on their understanding but each model drifts from the expected solution.

### Papers vs. Implementations

#### **1. DeepSeek R1 (PARC -** Research Report: Enhancing Mathematical Reasoning in Large Language Models through Premise-Augmented Verification)

My understanding of the Paper:

Imagine you’re solving a math problem step by step. Each step depends on what you did in the previous steps. This paper proposes a way to keep track of which older steps each new step relies on, so that a computer can:

1. Check each step against only the information it really needs (instead of rereading the entire solution).
2. Spot when a step _looks_ correct by itself but is actually built on a _wrong_ earlier step.
3. Mark the exact place(s) where things went wrong, instead of just saying “the final answer is wrong.”

This approach organizes a solution like a little map (a “directed acyclic graph”) connecting steps to the previous steps they depend on. Then a combined system—partly rule-based math checks, partly learned by a language model—verifies each step. The idea is that with a clear record of which facts lead to which conclusions, it’s easier to catch mistakes and to avoid spreading those mistakes through the rest of the solution.

* **Paper Claims**: Advanced premise-based math reasoning (DAG structure), distinguishing “native” vs. “accumulation” errors, improved step-level verification (91% precision, 84% recall).
* **Implementation Reality**: The provided code uses trivial numeric pattern checks (regex, minimal DeBERTa usage). **No** actual DAG or premise contamination logic is shown.
* **Real vs. Conceptual**:
  * _Conceptually plausible_ for math error detection.
  * _Largely unimplemented_ in the snippet; advanced claims remain theoretical.
* **Practical Value**: Could be valuable for advanced math if truly built, but code is incomplete.
* **Conclusion**: The code snippet is **far too minimal** to validate the advanced PARC claims. **Major portions** of the paper’s premise-based reasoning are either **conceptual or incomplete** in code. The proposed approach is plausible but under-implemented so we can assume that the results and claims are hallucinated or scraped form other papers, and overall it drifted for desired solution.

#### **2. OpenAI o1 (**&#x52;esearch Report: A Multi-Phase Reasoning Framework Demonstratio&#x6E;**)**

My understanding of the paper:

This paper shows a very **simple example** of teaching a small “GPT-4o-mini” model to solve **two types of tasks**—basic math and short code snippets—using **a few phases**:

1. **Initial Training:** They give the model a handful of examples so it learns how to format answers.
2. **Reward Setup:** They create a rule for judging success (is the math answer correct? does the code run and pass tiny tests?).
3. **Best-of-N Sampling:** They have the model try multiple solutions, then pick whichever works best.
4. **Lightweight RL:** They do a small update if the chosen solution is correct, nudging the model to repeat that solution style next time.

Because the tasks (like adding small numbers or writing a short Python function) are **very easy**, the model quickly reaches near-100% accuracy. The system acknowledges it’s just a minimal demonstration, not a full-blown RL system for complex tasks. But it shows how you can integrate **simple rewards** and **small updates** to push a model from “mostly correct” to “almost always correct,” at least for tiny toy problems.

* **Paper Claims**: Simple multi-phase RL pipeline for trivial code & arithmetic tasks. Pass@1 jumps from \~87% to 100%.
* **Implementation Reality**: The snippet does best-of-N sampling with random success changes, no real training or large-scale testing.
* **Real vs. Conceptual**:
  * Pipeline is _honestly minimal_ and matches disclaimers that tasks are small.
  * Gains come from artificially boosting success probability.
* **Practical Value**: Good _tutorial-style demonstration_, but _not_ an advanced or robust RL approach.
* **Conclusion**: The code snippet does **match** the paper’s disclaimers of a minimal, _tutorial-like demonstration._ Much of the “RL improvement” is artificially forced by manipulated probabilities. **Conceptually, it shows the multi-phase approach but no real model training or large-scale tasks, so this one also drifted from the desired solution and hallucinated.**

#### **3. OpenAI o1 (**&#x41; Minimal Open Reasoner for Code and Math: An 8-Section Research Paper)

My understanding of the paper:

This paper proposes a very simple framework (“minimal open reasoner”) that tackles two kinds of tasks at once:

1. **Code tasks** (like writing a “FizzBuzz” program) that get a “pass” or “fail.”
2. **Arithmetic tasks** (like small math word problems) that can be partially correct at each step and receive partial credit.

They keep a running collection (“aggregator”) of solutions that worked, then fine-tune the model again with those new, successful examples—so over time, it’s supposed to get better at both code and math. However, because the tasks in their demos are _very_ simple, the model quickly reaches a 100% pass rate, so there’s not much room to show true “iterative improvement.” Essentially, this paper shows a _template_ or _blueprint_ for how to set up code and math tasks in one pipeline, combine pass/fail rewards (for code) and step-by-step rewards (for math), and then keep track of good solutions for future training. But it’s still a very basic, toy-level demonstration.

* **Paper Claims**: Unifies code tasks (outcome-based reward) + arithmetic tasks (partial-step reward) under a single aggregator-based pipeline. Admits tasks are too small to show real iterative gain.
* **Implementation Reality**: Similar to the multi-phase snippet: random success, aggregator merges, and no true RL. Performance saturates quickly.
* **Real vs. Conceptual**:
  * _Conceptual approach_ to partial-step math + code pass/fail.
  * _Under-implemented_, mostly placeholders for aggregator loops.
* **Practical Value**: The idea is valid for bridging code + math in one pipeline, but the snippet is purely toy-level.
* **Conclusion**: The “Minimal Open Reasoner” paper’s approach sits **between** the short multi-phase demonstration and the aggregator expansions. It is **conceptually ok** but again “toy-level” or “placeholder” in code. The tasks saturate quickly, so they exhibit no iterative learning in practice, only hypothetical frameworks so looks **drifted and hallucinated**.



### **Comparison Table**

| **Criteria**                    | **DeepSeek R1 (PARC)**                                                                                | **OpenAI o1 (Multi-Phase)**                                                                                                                                                                                                                   | **Minimal Open Reasoner**                                                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **1. Paper’s Core Concept**     | DAG-based chain-of-thought verification in math (native vs. accumulation errors)                      | Tiny tasks, best-of-N + simple RL loop for code/arithmetic correctness                                                                                                                                                                        | Integrates code tasks (pass/fail) + math tasks (partial-step reward)                                                            |
| **2. Implementation Depth**     | Very minimal numeric checks, no DAG or premise-based logic                                            | Very minimal  random success, best-of-N sampling, no real gradient updates                                                                                                                                                                    | Very minimal similar random-based approach, aggregator merges, no actual training                                               |
| **3. Code vs. Paper Alignment** | Large mismatch: advanced premise approach vs. trivial snippet                                         | Generally aligns with disclaimers that it’s small & minimal, but still a large gap between paper and implementation                                                                                                                           | Concept matches the paper but remains toy-level with contrived improvements, still a large gap between paper and implementation |
| **4. Real vs. Made Up**         | Paper’s advanced claims appear mostly conceptual; snippet is superficial                              | Paper is transparent about trivial tasks; code uses forced random success                                                                                                                                                                     | Paper asserts a broad aggregator design, but code is again a mock approach                                                      |
| **5. Practical Applicability**  | Potentially high if truly built for math error detection; not shown in code                           | Good tutorial or teaching pipeline, too simple for real large tasks                                                                                                                                                                           | Conceptual bridging code + math tasks, quickly saturates for real usage                                                         |
| **6. Value as “Good Research”** | Interesting academically, but unverified claims and incomplete code implementation and hallucinations | Honest minimal example, not state-of-the-art, but unverified claims and trains gpt 4o which i think is not a real option so another one with unverified claims and hallucinations, it was the closest one but still very far from expectation | Broad conceptual approach, also toy-level; more expansions needed and unverified claims and hallucinations                      |

### Common Challenge: LLM Variability

* All three are generated by large language model–based “autonomous systems,” so each new run can spontaneously yield a slightly different approach or emphasis.
* Maintaining consistency across repeated “restarts” of the generation could require the same seed initialization and a human-in-the-loop to anchor key definitions, tasks, or partial code, but even this can produce variability.

### Improvements in Agentive Systems

* Redesigning the research agentive system with an emphasis on:&#x20;
  * Implementation and verification through directed workflows&#x20;
  * Improved memory management utilizing memory controllers&#x20;
  * Better flow control between components and account for dependency variability
  * A dynamic divide-and-conquer approach for all tasks, including automatic subtasks&#x20;
  * Utilizing graph databases for task breakdowns, connections, and status updates.&#x20;
  * Tree-based breakdowns with success path identification guided by RL or Judge models (other LLMs)
* Human-in-the-loop: The solutions you seek can be pretty opinionated, and all solutions contain both subjective and objective properties. This means that you desire your solutions to be grounded in truth—accurate and reliable—while also adhering to a specific style. This allows for potential integration into other systems or ensures that outputs are produced in specific formats. You expect them to maintain a particular structure for enhanced maintainability, testability, and increased trust in the solutions provided.&#x20;
* Leveraging more advanced tools such as [SymbolicA](https://symbolicai.readthedocs.io/en/latest/INTRODUCTION.html)[I ](https://symbolicai.readthedocs.io/en/latest/INTRODUCTION.html)that are actually more suitable for these kinds of tasks and offer more granular control than other frameworks with a lot of tooling built around LLMs, some of the key features are:
  * Seamless transition between differentiable and classical programming
  * Neuro-symbolic computation using LLMs
  * Composable operations for complex problem-solving
  * Integration with various engines (OpenAI, WolframAlpha, OCR, etc.)
  * Support for multimodal inputs and outputs

**Key Takeaways**:

* **DeepSeek R1** (PARC) is the most ambitious in math reasoning but shows the greatest gap between its advanced paper claims and simple snippet.
* **OpenAI o1 (Multi-Phase)** is straightforward, with its paper and code both presenting a toy RL approach; this was the closest one between the three, but there is still a large gap between claims and implementation.
* **Minimal Open Reasoner** extends the multi-phase concept to partial-step rewards for math plus code tasks, still a large gap between claims and implementation.
* None of them could handle the complexity of the task, and I believe it was due to a combination of both model instruction following and bad design of the agentive system for very complex tasks, which could work for simpler ones, but we wanted to test the limits.
* Although all solutions somewhat follow that four-service structure that we wanted, their methods and focuses vary greatly. This variation, along with their respective vulnerabilities to “hallucination”,  and solution drift, indicates that while I found some ideas intriguing, the results deviated from my expectations, the anticipated framework development process, and the implementation of each paper were too simplistic to enforce the claims the system maked in the papers.&#x20;
* While Agent Laboratory may not be the right tool for fully developing this type of system, we were primarily interested in the research aspect, the thinking, and the experimentation that these models would explore to determine whether they could provide valuable ideas worth further investigation or if they would be similar to the concepts we are already examining while working on an **Integrated Reasoner Framework** on **Apolo Cloud.**

**Overall, each approach is partly conceptual and under-implemented for real-world or advanced usage, and claims are inflated and unverified. These systems are still useful to get new ideas out, and with humans in the loop and more advanced workflows, I could see how these systems would yield better and better results. I tested it on a very complex task, it should work better on simpler ones.**

### Resources

**I'll attach the file for DeepSeek R1**:&#x20;

* Research Report: Enhancing Mathematical Reasoning in Large Language Models through Premise-Augmented Verification

{% file src="../.gitbook/assets/Deepseek R1 (2).pdf" %}

**OpenAI o1 files**:

* A Minimal Open Reasoner for Code and Math: An 8-Section Research Paper

{% file src="../.gitbook/assets/OpenAI o1 first paper.pdf" %}

* Research Report: A Multi-Phase Reasoning Framework Demonstration

{% file src="../.gitbook/assets/OpenAI o1 second paper.pdf" %}

The implementations and papers can be found [here](https://github.com/neuro-inc/AgentLaboratory) too, under the `projects/` folder.








---
File: /use-cases/llms/deepseek-r1-distilled-models.md
---

---
icon: whale
---

# DeepSeek-R1 distilled models

Large language models (LLMs) have become essential tools for AI applications, but deploying them efficiently remains a challenge. [DeepSeek](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d) Distilled models offer a balance between performance and efficiency, making them ideal for various real-world use cases.

In this guide, we will walk through deployment process of DeepSeek Distilled LLMs using [vLLM](https://github.com/vllm-project/vllm) on the **Apolo** platform.

Apolo simplifies deployment by handling:

* **Resource Allocation** – Ensuring requested GPU and CPU are always available.
* **Workload Scheduling** – Dynamically managing inference jobs.
* **Orchestration & Isolation** – Serving models endpoints securely in isolated environments.
* **Ingress & Authentication** – Providing built-in API access control and request routing.

## Hardware Considerations

Since Apolo abstracts infrastructure management, you won’t need to configure hardware manually. Instead, you operate on resource presets that incorporate a collection of resources available at runtime. For high-performance inference, consider utilizing Apolo resource preset with:

* **GPU:** NVIDIA A100 (40GB), H100, or RTX 4090. VRAM requirements depend on the model and the required context length. Minimum of 24GB VRAM recommended.
* **CPU:** At least 8 vCPUs for handling requests efficiently.
* **RAM:** 32GB+ for handling larger batch sizes or concurrent requests.
* **Storage:** consider utilizing Apolo storage that is backed by high-throughput SSD/NVMe to persist model binaries and for faster startups.

In this guide we will be outlining 3 distinct ways to deploy Large Language Models on Apolo platform, you can choose one that suits you most or try all three:

* **Deploy with CLI**
* **Deploy with Apolo-Flow**
* **Deploy with Apps GUI**

By the end of this guide, you’ll have a fully operational DeepSeek Distilled model deployed on Apolo, serving inference requests efficiently with vLLM.

Let’s get started!

## Deploy with Apolo CLI

The easiest way to start the server is to utilize CLI.

First, make sure you've completed the getting-started guide from the main documentation page since here we assume that you already installed Apolo CLI, logged into the platform, created (or joined ) organization and project.

Second, pick the resource preset you want to run you server on. For this, checkout the Apolo cluster settings either in web console, or via CLI command `apolo config show`.

In this example, we have the following presets that could do the work:

```bash
$ apolo config show
User Configuration:                                         
...
Resource Presets:                                                                   
 Name          #CPU     Memory   GPU                                Credits per hour 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
...
 H100x1        25.0   250.0 GB   Nvidia: 1 x Nvidia-DGX-H100-80GB   6.08             
 H100x2        50.0   500.0 GB   Nvidia: 2 x Nvidia-DGX-H100-80GB   12.16            
 H100x4       100.0     1.0 TB   Nvidia: 4 x Nvidia-DGX-H100-80GB   24.32            
 dgx            220     2.1 TB   Nvidia: 8 x Nvidia-DGX-H100-80GB   48.64  
```

### deepseek-ai/DeepSeek-R1-Distill-Llama-70B

70B Llama model requires around 140 GB of vRAM in FP16 format. Therefore, we use H100x2 here.

To start vLLM server, use the following CLI command:

{% code fullWidth="true" %}
```bash
$ apolo run -s H100x2 -v storage:hf-cache:/root/.cache/huggingface --http-port 8000 vllm/vllm-openai -- '
    --model=deepseek-ai/DeepSeek-R1-Distill-Llama-70B 
    --dtype=half 
    --tensor-parallel-size=2 
    --max-model-len=1000'
```
{% endcode %}

The rest will be done by the platform: it allocates the resources, creates needed job, starts the server, exposes the endpoint, collects the metrics and so on...

Brief break down of the command:

* `-s H100x2` specifies the preset hardware config name that will be used while running the job.
* `-v storage:hf-cache:/root/.cache/huggingface` mounts the platform storage folder `hf-cache` into the job's filesystem under /root/.cache/huggingface. This is where vLLM looks for model binaries on the startup.
* `--http-port 8000` tells Apolo which port from within the job to expose.
* `vllm/vllm-openai`is a container image name, used to run the job.

The rest of the command are vLLM arguments. Full description could be found in the corresponding [section](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#cli-reference) of vLLM documentation.

Upon the successful activation of the command you should see the following output:

```bash
√ Job ID: job-5ce4cc22-11e8-457a-8c70-bc1af64a2b3a
- Status: pending Creating
- Status: pending Scheduling
- Status: pending Pulling (Pulling image "vllm/vllm-openai:latest")
√ Status: running
√ Http URL: https://job-5ce4cc22-11e8-457a-8c70-bc1af64a2b3a.jobs.cl1.org.apolo.us
√ =========== Job is running in terminal mode ===========
...
```

Note the 'Http URL'. - this is the endpoint to direct your queries to once the job is fully up and running.

You will see the following line when the server is ready to accept requests:

```
...(other server logs)...
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Query the model

When the model is up and running, you could use any standard client to query it. In this example, we use `curl`to send the request:

{% code fullWidth="true" %}
```bash
curl -s https://job-5bd3ab12-7c94-4e3a-85eb-e56e6320c1b0.jobs.cl1.org.apolo.us/v1/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer `apolo config show-token`" \
    -d '{
        "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
        "prompt": "San Francisco is a",
        "max_tokens": 100,
        "temperature": 0
    }' | jq
{
  "id": "cmpl-b866939698bd4cc59e5ffbb4548ecba0",
  "object": "text_completion",
  "created": 1739486182,
  "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
  "choices": [
    {
      "index": 0,
      "text": " city that is known for its iconic landmarks, cultural diversity, and vibrant neighborhoods.",
      "logprobs": null,
      "finish_reason": "length",
      "stop_reason": null,
      "prompt_logprobs": null
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 105,
    "completion_tokens": 100,
    "prompt_tokens_details": null
  }
}
```
{% endcode %}

Note, the usage of authorization header ("Authorization: Bearer...") is obligatory here, however, you could disable it. See the description of all possible job parameters and configurations in Apolo CLI documentation.

To cleanup hit ctrl+c in the console window, where the job was launched. Alternatively, use cli command:

`apolo kill <job-id>`

to terminate the job.

This is it! You now have a fully operational DeepSeek Distilled model deployed on Apolo, serving inference requests efficiently with vLLM!

## Deploy with Apolo Flow

Apolo Flow allows one to template the workloads configuration into config files. By the end of the getting-started guide, you should be able to create and run a flow from the template. The below scenario combines exposing DeepSeek Distilled model and making querying it in browser available via custom WebUI interface.

For this scenario, we need to create a flow with the following components:

* Apolo storage volumes that host model binaries and web server files
* vLLM server that serves the requests, exactly the same as we did previously
* [OpenWebUI](https://openwebui.com/) server that acts as a web interface where you could chat with your model.

Here is the configuration file snipped that implements those things:

```yaml
kind: live

volumes:
  webdata:
    remote: storage:$[[ flow.project_id ]]/web
    mount: /app/backend/data
    local: webdata
  hf_cache:
    remote: storage:$[[ flow.project_id ]]/cache
    mount: /root/.cache/huggingface

jobs:
  web:
    image: ghcr.io/open-webui/open-webui:v0.5.11
    volumes:
      - ${{ volumes.webdata.ref_rw }}
    http_port: 8080
    preset: cpu-small
    detach: true
    browse: true
    env:
      WEBUI_SECRET_KEY: "apolo"
      OPENAI_API_BASE_URL: http://${{ inspect_job('vllm').internal_hostname_named }}:8000/v1 # inspects vllm job in runtime to derive endpoint domain address

  vllm:
    image: vllm/vllm-openai:v0.7.2
    preset: ${{ params.preset }}
    http_port: "8000"
    detach: true
    volumes:
      - ${{ volumes.hf_cache.ref_rw }}
    env:
      HF_TOKEN: secret:HF_TOKEN # your huggingface token used to pull models, could be added with `apolo secret add HF_TOKEN <token>`
    params:
      preset: H100x2 # replace the preset during the job startup via `apolo-flow run vllm --param preset <preset-name>`
    cmd: >
      --model deepseek-ai/DeepSeek-R1-Distill-Llama-70B 
      --tokenizer deepseek-ai/DeepSeek-R1-Distill-Llama-70B
      --dtype=half
      --tensor-parallel-size=2
      --max-model-len=10000
```

You could find full configuration file in our GitHub [repository.](https://github.com/neuro-inc/mlops-open-webui)

The overall description of flow configuration syntax could be found in a dedicated documentation page. Let's now start `vllm`and `web` jobs.

```bash
$ apolo-flow run vllm
√ Job ID: job-73404eb1-1606-4c46-9641-e4895cc2010a
√ Name: openwebui-vllm
- Status: pending Creating
- Status: pending Scheduling
√ Status: running
√ Http URL: https://vllm--0e1436ea6a.jobs.cl1.org.apolo.us
√ The job will die in 10 days. See --life-span option documentation for details.
```

You can observe server startup process by connecting to the logs stream using cli command:

`apolo-flow logs vllm`.

### Query the model

In this case, we describe another approach to "consume" the service provided by the LLM inference server. Here we start the OpenWebUI web server, that resembles OpenAI's ChatGPT application. It allows you to chat with various LLM servers at the same time, including OpenAI-compatible (which vLLM is) and Ollama APIs.

To start web chat with your DeepSeek model, issue cli command:

`apolo-flow run web --param server vllm`

```bash
$ apolo-flow run web
√ Job ID: job-df1f8339-6c99-4ee8-b425-1daa7e023d8b
√ Name: openwebui-web
- Status: pending Creating
- Status: pending Scheduling
- Status: pending Pulling (Pulling image "ghcr.io/open-webui/open-webui:v0.5.11")
- Status: pending ContainerCreating
√ Status: running
√ Http URL: https://openwebui-web--0e1436ea6a.jobs.cl1.org.apolo.us
√ The job will die in 10 days. See --life-span option documentation for details.
```

Now the mentioned above OpenWebUI job's URL will be automatically opened in your default browser. After you log into the system, you will be able to chat with your model. Just make sure vllm finished it startup.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p>OpenWebUI attached to vLLM serving deepseek-ai/DeepSeek-R1-Distill-Llama-70B</p></figcaption></figure>

This is it! You have crated and ran a flow from template, your flow has spun up a DeepSeek distilled model using vLLM and exposed its interface via web browser using OpenWebUI web-server app.

## Deploy with Apolo Apps GUI

Apolo applications allow you to deploy various systems together with their auxiliary resources as a holistic application. This also includes LLM model inference servers that enables scaling and reliability required for the production-ready projects.

The deployment process itself is quite straightforward: navigate to the Apolo web console, select LLM Inference application and start installation.

The following configuration screenshot resembles the previously discussed case:

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption><p>LLM Inference application configuration</p></figcaption></figure>

After the installation completes, you can find the endpoint for inference in application outputs.

## Deploy other DeepSeek-R1 distilled models

To deploy any other model, simply derive the amount of required vRAM to fit the model. Afterwards, select a corresponding resource preset and adjust vLLM CLI arguments. For vLLM you might need to tweak the number tensor parallel replicas as well as context length (max-model-len).

The rest stays the same — Apolo takes care of operations leaving you focused on the job.



---
File: /use-cases/llms/deepseek-r1-model-deployment.md
---

---
icon: whale
---

# DeepSeek-R1 model deployment

In this guide, we will walk through deployment process of DeepSeek R1 model using [vLLM](https://github.com/vllm-project/vllm) and [Ray](https://docs.ray.io/en/latest/ray-overview/getting-started.html) on the **Apolo** platform.

**DeepSeek-R1** is a large language model that, [according to it's developers](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf), achieves performance comparable to OpenAI-o1 across math, code, and reasoning tasks. The model was trained via large-scale reinforcement learning without supervised fine-tuning as a preliminary step.

## Hardware Considerations

DeepSeek-R1 model way exceeds the memory capacity of a single GPU or even the entire DGX (NVIDIA's full-fledged AI machine). The model has 671 Billion parameters therefore it requires \~ 1.3 TB of vRAM only to host it's weights in an original format. It also has 128K tokens [context size](#user-content-fn-1)[^1] capacity, which bloats the memory requirements even further.

You could estimate your model vRAM requirements using any on-line calculator, for instance [ollama-gpu-calculator](https://aleibovici.github.io/ollama-gpu-calculator/).

For most of the use-cases it's more efficient to host a quantized version of the model that drastically reduces the memory requirements and speeds-up the inference process slightly sacrificing a quality of the results. Here we are going to deploy an AWQ-quantized version of the DeepSeek-R1 model ([cognitivecomputations/DeepSeek-R1-AWQ](https://huggingface.co/cognitivecomputations/DeepSeek-R1-AWQ)). We are going to use two NVIDIA DGX nodes with 8 x NVIDIA Tesla H100 SMX cards (80 Gb of vRAM) within which in sum gives us approx 1.2 TB of vRAM, more than enough to fit the model at full context length.

If you have access to a different resource pools in your cluster, you should first find out how many workers should be connected to the Ray cluster. You better use the same resource preset to split the load evenly. Here is what you need to do:

1. &#x20;Identify the amount of vRAM each GPU has. Either from the GPU model, or manually:

```
$ apolo run --preset <your-preset> ubuntu -- nvidia-smi
Using preset '<your-preset>'
Using image 'ubuntu:latest'
√ Job ID: job-7f36c1c3-f21e-4d14-9e59-8a69079bae22
- Status: pending Creating
- Status: pending Scheduling
- Status: pending ContainerCreating
√ Status: running Restarting
√ Http URL: https://job-7f36c1c3-f21e-4d14-9e59-8a69079bae22.jobs.cluster.org.apolo.us
√ The job will die in a day. See --life-span option documentation for details.

√ =========== Job is running in terminal mode ===========
√ (If you don't see a command prompt, try pressing enter)
√ (Use Ctrl-P Ctrl-Q key sequence to detach from the job)
Tue Feb 25 21:13:10 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-80GB          Off |   00000000:81:00.0 Off |                    0 |
| N/A   25C    P0             64W /  500W |      13MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A100-SXM4-80GB          Off |   00000000:C1:00.0 Off |                    0 |
| N/A   22C    P0             57W /  500W |      13MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
√ Job job-7f36c1c3-f21e-4d14-9e59-8a69079bae22 finished successfully
```

In this case, we have 2 GPUs with 80 GB of vRAM each. This means, to you will need to have \~ 7 workers running on this preset (assuming we need 1.2 Tb of vRAM).

## Software Consideration

We are going to run vLLM inference server on top of the Apolo platform. As you know, Apolo simplifies deployment by handling resource allocation, workloads scheduling, orchestration & isolation of processes and provisioning ingress and authentication capabilities.

We are also going to leverage [Ray](https://docs.ray.io/en/latest/ray-overview/getting-started.html), a distributed computing framework that enables multi-GPU and multi-node inference to serve the model at a full context-length configuration, which is often required for the advanced tasks.

Here is a diagram overview of what we are trying to achieve:

<figure><img src="../.gitbook/assets/Apolo DeepSeek-R1 deployment diagram.svg" alt=""><figcaption><p>Apolo DeepSeek-R1 Ray deployment diagram</p></figcaption></figure>

Please note, if you don't have an access to such a resource preset, a generic guideline for building Ray cluster capable enough is to:

* Run all jobs on the same preset, so the hardware stays heterogeneous
* Set `--pipeline-parallel-size` to the number of jobs dedicated for your cluster, including the head job.
* Set `--tensor-parallel-size` to the number of GPUs in each job.
* The overall vRAM capacity should be around 1.2 Tb for inference on a full context length. You could reduce it by lowering the context length.

## Deploy with Apolo CLI

The easiest way to start is to utilize CLI.

Before going further, make sure you've completed the getting-started guide from the main documentation page, installed Apolo CLI, logged into the platform, created (or joined) organization and project.

Please note, the deployment consists of two main components: Ray head job and Ray worker job, which together form a static Ray cluster for hosting the vLLM server. Within a Ray worker node we will launch vLLM server that will be spread across the virtual cluster.

**First**, let's start a Ray head job:

{% code overflow="wrap" fullWidth="true" %}
```bash
apolo run --preset dgx --name ray-head --life-span 10d -v storage:hf-cache:/root/.cache/huggingface -e HF_TOKEN=secret:HF_TOKEN --entrypoint ray vllm/vllm-openai:v0.7.2 -- start --block --head --port=6379
```
{% endcode %}

Brief break down of the command:

* `-s dgx` specifies the preset hardware config name that will be used while running the job.
* `--life-span 10d` configures for how long should Apolo run the job.&#x20;
* `-v storage:hf-cache:/root/.cache/huggingface` mounts the platform storage folder `hf-cache` into the job's filesystem under /root/.cache/huggingface. This is where vLLM looks for model binaries on the startup.
* `--entrypoint ray`  overwrites a default entrypoint of the container image to `ray` executable.
* `vllm/vllm-openai`is a container image name, used to run the job.
* `start --block --head --port=6379` is a command arguments sent to `ray` executable.

After the scheduling, a Ray head job will start waiting for the incoming connections and serving the requests. Leave it for now running.

Before going further, note the output of the following command:

{% code fullWidth="false" %}
```
$ apolo status ray-head                                                                 
 Job                      job-324eab93-5fec-4cf6-bda5-3b6c701162bb                  
 Name                     ray-head  
...    
 Image                    vllm/vllm-openai:v0.7.2      
 Entrypoint               ray      
 Command                  start --block --head --port=6379 --dashboard-host=0.0.0.0 
 Preset                   dgx        
 Resources                 Memory                                2.1 TB             
                           CPU                                    220.0               
                           Nvidia GPU          8 x Nvidia-DGX-H100-80GB              
                           Extended SHM space                      True               
 Life span                10d                                   
 TTY                      True      
 Volumes                   /root/.cache/huggingface  storage:ollama_server/cache
 Internal Hostname        job-324eab93-5fec-4cf6-bda5-3b6c701162bb.platform-jobs
 Internal Hostname Named  ray-head--0e1436ea6a.platform-jobs <<=== THIS ONE! <====
 Http URL                 https://ray-head--0e1436ea6a.jobs.cl1.org.apolo.us 
 ...
```
{% endcode %}

It derives a runtime information from the running job on the platform. We are particularly interested in `Internal Hostname named` row. This is a domain name within the cluster, needed for the worker job to connect to the head.

**Second**, let's start a Ray worker(s) node(s). If you need more than one worker nodes, you should start all of them but one now. If you are good with only one worker, proceed to the next step.

Open a new console window and copy-paste the following command. Please parameterize the address of your Ray head job accordingly.

{% code overflow="wrap" fullWidth="true" %}
```bash
$ apolo run --preset <your-preset> --tag ray-worker -v storage:hf-cache:/root/.cache/ -e HF_TOKEN=secret:HF_TOKEN --life-span 10d --detach vllm/vllm-openai:v0.7.2 -- start --address=ray-head--0e1436ea6a.platform-jobs:6379 --block
```
{% endcode %}

**Third,** let's start last Ray worker, that will also start the model deployment. The model's endpoint will be hosted at this job, therefore, you should use this job's host URL to send the requests.

Run the following command in your console:

{% code overflow="wrap" fullWidth="true" %}
```bash
$ apolo run --preset dgx --http-port 8000 --no-http-auth --name ray-worker -v storage:hf-cache:/root/.cache/huggingface --entrypoint bash -e HF_TOKEN=secret:HF_TOKEN --life-span 10d vllm/vllm-openai:v0.7.2 \
-- -c '
ray start --address=ray-head--0e1436ea6a.platform-jobs:6379; python3 -m vllm.entrypoints.openai.api_server --model cognitivecomputations/DeepSeek-R1-AWQ --tokenizer cognitivecomputations/DeepSeek-R1-AWQ --dtype=float16 --tensor-parallel-size=8 --pipeline-parallel-size=2 --trust-remote-code --max-model-len=128000 --enforce-eager
'
```
{% endcode %}

This instructs Apolo to start Ray worker Job on another DGX machine (unless you change the preset name). Within this job, we will also launch vLLM server on top of the running Ray cluster that will utilize a high-throughput intra-cluster communication (InfiniBand) protocol to serve a model distributed onto two machines. The startup process might take some time, depending on your cluster settings.

You will see the following line when the server is ready to accept requests:

```bash
...(other server logs)...
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Query the model

When the model is up and running, you could use any standard client to query it. To derive the endpoint for sending the request, check the status of a ray-worker job:

<pre data-full-width="false"><code><strong>$ apolo status ray-worker
</strong> Job                      job-5cf69164-0f64-4d3f-8354-b4d02ee0c8f8                                                                                                                                                 
 Name                     ray-worker                                                                                                                                                                               
 ...
 Image                    vllm/vllm-openai:v0.7.2                                                                                                                                                                  
 Entrypoint               bash                                                                                                                                                                                     
 Command                  -c 'ray start --address=ray-head--0e1436ea6a.platform-jobs:6379                                                                                                                          
                            python3 -m vllm.entrypoints.openai.api_server --model cognitivecomputations/DeepSeek-R1-AWQ --tokenizer cognitivecomputations/DeepSeek-R1-AWQ --dtype=float16 --tensor-parallel-size=8 
                          --pipeline-parallel-size=2 --trust-remote-code --max-model-len=100000 --enforce-eager'                                                                                                   
 Preset                   dgx                                                                                                                                                                                      
 Resources                 Memory                                2.1 TB                                                                                                                                            
                           CPU                                    220.0                                                                                                                                            
                           Nvidia GPU          8 x Nvidia-DGX-H100-80GB                                                                                                                                            
                           Extended SHM space                      True                                                                                                                                            
 Life span                10d                                                                                                                                                                                      
 .TTY                      True                                                                                                                                                                                     
 Volumes                   /root/.cache/huggingface  storage:ollama_server/cache                                                                                                                                   
 Internal Hostname        job-5cf69164-0f64-4d3f-8354-b4d02ee0c8f8.platform-jobs                                                                                                                                   
 Internal Hostname Named  ray-worker--0e1436ea6a.platform-jobs                                                                                                                                                     
 Http URL                 https://ray-worker--0e1436ea6a.jobs.cl1.org.apolo.us &#x3C;&#x3C;=== THIS ONE! &#x3C;====
</code></pre>

There you are going to see  a public domain name of the job, at the `Http URL` row. Now, let's use `curl`to send the request:

```bash
curl -s https://ray-worker--0e1436ea6a.jobs.cl1.org.apolo.us/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "cognitivecomputations/DeepSeek-R1-AWQ",
        "prompt": "San Francisco is a",
        "max_tokens": 100,
        "temperature": 0
    }' | jq
{
  "id": "cmpl-ecb0b36cd86c454b95bf62a269e95848b3f9",
  "object": "text_completion",
  "created": 1739913613,
  "model": "cognitivecomputations/DeepSeek-R1-AWQ",
  "choices": [
    {
      "index": 0,
      "text": " city that is known for its iconic landmarks, cultural diversity, and vibrant neighborhoods.",
      "logprobs": null,
      "finish_reason": "length",
      "stop_reason": null,
      "prompt_logprobs": null
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 105,
    "completion_tokens": 100,
    "prompt_tokens_details": null
  }
}
```

To cleanup hit ctrl+c in the console windows, where the jobs were launched. Alternatively, use cli commands:

* `apolo ps` to list your running jobs
* `apolo kill <job-id1> <job-id2> ...` to terminate the job(s)

This is it! You now have a fully operational DeepSeek R1 distributed model deployment on Apolo, serving inference requests efficiently with vLLM!

## Deploy with Apolo Flow

Apolo Flow allows one to template the workloads configuration into config files. The below configuration file snippet arranges the previously discussed deployment process in a couple of Apolo-Flow job descriptions. We also expand this scenario with the deployment of [OpenWebUI](https://openwebui.com/) server that acts as a web interface for chatting with your models.

You should also adjust the preset names according to the [#hardware-considerations](deepseek-r1-model-deployment.md#hardware-considerations "mention").

{% code fullWidth="false" %}
```yaml
kind: live

defaults:
  life_span: 10d

volumes:
  webdata:
    remote: storage:$[[ flow.project_id ]]/web
    mount: /app/backend/data
    local: webdata
  hf_cache:
    remote: storage:$[[ flow.project_id ]]/cache
    mount: /root/.cache/huggingface

jobs:
  web:
    image: ghcr.io/open-webui/open-webui:v0.5.11
    volumes:
      - ${{ volumes.webdata.ref_rw }}
    http_port: 8080
    preset: cpu-small
    detach: true
    browse: true
    env:
      WEBUI_SECRET_KEY: "apolo"
      OPENAI_API_BASE_URL: http://${{ inspect_job('ray-worker').internal_hostname_named }}:8000/v1 # inspects vllm job in runtime to derive endpoint domain address

  ray_head:
    image: vllm/vllm-openai:v0.7.2
    name: ray-head
    preset: dgx
    detach: true
    life_span: 10d
    http_port: "8000"
    volumes:
      - ${{ volumes.hf_cache.ref_rw }}
    env:
      HF_TOKEN: secret:HF_TOKEN # your huggingface token used to pull models, could be added with `apolo secret add HF_TOKEN <token>`
    entrypoint: ray
    cmd: >
      start --block --head --port=6379 --dashboard-host=0.0.0.0

  ray_extra_worker:
    image: vllm/vllm-openai:v0.7.2
    preset: dgx
    multi: true
    detach: true
    http_port: "8000"
    http_auth: false
    life_span: 10d
    volumes:
      - ${{ volumes.hf_cache.ref_rw }}
    env:
      HF_TOKEN: secret:HF_TOKEN
    cmd: >
      ray start --address=${{ inspect_job('ray_head').internal_hostname_named }}:6379

  ray_worker:
    image: vllm/vllm-openai:v0.7.2
    name: ray-worker
    preset: dgx
    detach: true
    http_port: "8000"
    http_auth: false
    life_span: 10d
    volumes:
      - ${{ volumes.hf_cache.ref_rw }}
    env:
      HF_TOKEN: secret:HF_TOKEN
    entrypoint: bash
    cmd: >
      -c 'ray start --address=${{ inspect_job('ray_head').internal_hostname_named }}:6379
        python3 -m vllm.entrypoints.openai.api_server --model cognitivecomputations/DeepSeek-R1-AWQ --tokenizer cognitivecomputations/DeepSeek-R1-AWQ --dtype=float16 --tensor-parallel-size=8 --pipeline-parallel-size=2 --trust-remote-code --max-model-len=100000 --enforce-eager'

```
{% endcode %}

You could find full configuration file in our GitHub [repository.](https://github.com/neuro-inc/mlops-open-webui)

Now start `ray_head`, `ray_worker` and `web` jobs. Please give Ray a minute to spin-up a Head job before continuing with the worker node.

```bash
apolo-flow run ray_head # wait a munite after running head job, so it starts
apolo-flow run ray_extra_worker # run extra workers if needed
apolo-flow run ray_worker # it will connect to the ray_head and start the model
apolo-flow run web # this will attach to the worker node 
```

As in previous case, give vLLM some time to load such a huge LLM model into the GPU memory.

You can observe server startup process by connecting to the logs stream using cli command:

```bash
apolo-flow logs ray_worker
```

You will see the following line when the server is ready to accept requests:

```bash
...(other server logs)...
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Query the model

You could use any client that best fits your needs. You could also notice that a web page with OpenWebUI was opened in your default browser. There you could query your model:&#x20;

<figure><img src="../.gitbook/assets/deepseek-inference.gif" alt=""><figcaption><p>DeepSeek-R1 inference process</p></figcaption></figure>

That's it!\
Now you know how to spin-up the DeepSeek-R1 model using vLLM and exposed its interface via web browser using OpenWebUI web-server app.

Don't forget to terminate the launched jobs when you don't need it:

```bash
apolo-flow kill ALL
```

This will terminate all jobs launched in this flow.



[^1]: "memory" of the LLM, its "inputs"



---
File: /use-cases/llms/teaching-models-to-reason-training-fine-tuning-and-evaluating-models-with-llama-factory-on-apolo.md
---

---
description: This is a tutorial for training, fine-tuning and evaluating models.
---

# Teaching Models To Reason - Training, Fine-Tuning, and Evaluating Models with LLaMA Factory on Apolo

This tutorial will guide you through **training, fine-tuning, and evaluating models** using **LLaMA Factory on the Apolo platform**. By the end, you will be able to:

* **Deploy LLaMA Factory on Apolo**
* **Train and fine-tune models using Web UI or CLI**
* **Evaluate and test your trained models**
* **Serve the fine-tuned model via API for real-world applications**

### **Prerequisites**

Before proceeding, ensure you have: \
✅ **Apolo CLI installed** (Follow the Apolo CLI[ Installation Guide](https://docs.apolo.us/index/cli/installing))\
✅ [**Docker**](https://docs.docker.com/engine/install/) **installed** for building images \
✅ **An Apolo project is set up** (will use current project if no project is set)\
✅ **A HuggingFace token set as a secret** You can do that by running the following command

```
apolo secret add HF_TOKEN <your_token>
```

### **1. Deploying LLaMA Factory on Apolo**

#### **Step 1: Clone the LLaMA Factory Repository**

```bash
git clone https://github.com/neuro-inc/LLaMA-Factory
cd LLaMA-Factory
```

Inside the apolo branch you will notice a  .`apolo`  folder containing a `live.yaml`. You can find more on the structure of the file below [here](https://docs.apolo.us/index/apolo-flow-reference/workflow-syntax/live-workflow-syntax).

```yaml
kind: live
title: llama_factory

defaults:
  life_span: 5d

images:
  llama_factory:
    ref: image:$[[ project.id ]]:v1
    dockerfile: $[[ flow.workspace ]]/docker/docker-cuda/Dockerfile
    context: $[[ flow.workspace ]]/

volumes:
  hf_cache:
    remote: storage:$[[ flow.project_id ]]/hf_cache
    mount: /root/.cache/huggingface
    local: hf_cache
  data:
    remote: storage:$[[ flow.project_id ]]/data
    mount: /app/data
    local: data
  output:
    remote: storage:$[[ flow.project_id ]]/output
    mount: /app/saves
    local: output

jobs:
  llama_factory_webui:
    image: ${{ images.llama_factory.ref }}
    name: llama-factory
    preset: H100X1
    http_port: "7860"
    detach: true
    browse: true
    env:
      HF_TOKEN: secret:HF_TOKEN
    volumes:
      - ${{ upload(volumes.data).ref_rw }}
      - ${{ volumes.output.ref_rw }}
      - ${{ volumes.hf_cache.ref_rw }}
    cmd: bash -c "cd /app && llamafactory-cli webui"

```

Key fields to consider when deploying LlamaFactory on Apolo:

* `preset`  In this case we have H100X1 (Requests a single NVIDIA H100 GPU.)\
  to list all available presets on your cluster you can use:

```
apolo config show
```

* `data` volume, this will upload everything you have in the data folder to the jobs `/app/data`
* `output` volume, this is where you can save your checkpoints and training artifacts, the job will write to this folder /app/saves

#### **Step 2: Build the LLaMA Factory Docker Image on Apolo**

```bash
apolo-flow build llama_factory
```

This command:

* Uses the **Dockerfile configured for CUDA** (located at `docker/docker-cuda/Dockerfile`).
* Pushes the built image to the **Apolo image registry**.

**Output Example**:

```bash
[0600] Pushing image to registry.<your_cluster_name>.org.apolo.us/apolo/<your_project_name>/llama_factory:v1 
INFO[0611] Pushed registry.<your_cluster_name>.org.apolo.us/apolo/<your_project_name>/llama_factory@sha256:6cc93e18...
INFO: Successfully built image: llama_factory:v1
```

**Note:**  If you need to work with other datasets that are not supported by default, you should add support for them by extending the `dataset_info.json`. This file allows for field mapping and format type selection. I added open-r1/OpenR1-Math-220k, a reasoning dataset that will be used to finetune a Llama 3B model to enhance its reasoning capabilities.

<pre class="language-json"><code class="lang-json"><strong>{
</strong>
"open-r1/OpenR1-Math-220k": {
      "hf_hub_url": "open-r1/OpenR1-Math-220k", 
      "formatting": "sharegpt",
      "ranking": false,
      "split": "train", // use test split if available in the dataset
      "columns": {
        "messages": "messages"  
      },
      "tags": {
        "role_tag": "role",
        "content_tag": "content",
        "user_tag": "user",
        "assistant_tag": "assistant",
        "system_tag": "system"
      }
    }
}

</code></pre>



#### **Step 3: Run the LLaMA Factory Web UI**

```bash
apolo-flow run llama_factory_webui
```

This will:

* Copy necessary datasets and configurations to Apolo storage.
* Start the **llama\_factory\_webui** job.

**Output Example**:

```bash
√ Job ID: job-f6522c71-1912-4775-962e-19f3c1357224
√ Name: llama-factory
√ Status: running
√ Http URL: https://llama-factory--0214c319f8.jobs.<your_cluster_name>.org.apolo.us
```

#### **Step 4: Access the Web UI**

**You can either use the URL above, which is part of the deployment output or wait for a new tab to open automatically with the Llama Factory Web UI, as seen below.**



<figure><img src="../.gitbook/assets/Screenshot 2025-02-13 at 14.14.35.png" alt=""><figcaption></figcaption></figure>

🎉 **You are now ready to train and fine-tune models!**

### **2. Training & Fine-Tuning Models with LLaMA Factory**

#### **Option 1: Fine-Tuning Using the Web UI**

Once inside the Web UI:

**Step 1: Select Base Model**

* Choose a **base model** (e.g., `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B, Llama-3.2-3B`).
* Specify the **model path** (Hugging Face model).

**Step 2: Choose Training Method**

* **Full** (for training all parameters).
* **LoRA** (lightweight, efficient fine-tuning).
* **Freeze (freeze certain layers, there's a section on freezing layers in the UI).**

**Step 3: Configure Dataset**

* Select a **built-in dataset** or provide a **custom dataset,** we''ll go with the open-r1/OpenR1-Math-220k dataset for which we added support.
* Click **"Preview Dataset"** to verify.

<figure><img src="../.gitbook/assets/Screenshot 2025-02-18 at 13.29.56.png" alt=""><figcaption></figcaption></figure>

**Step 4: Set Training Hyperparameters**

| Parameter                 | Recommended Value         |
| ------------------------- | ------------------------- |
| **Learning Rate**         | `5e-5`                    |
| **Epochs**                | `3`                       |
| **Batch Size**            | `2` (adjust based on GPU) |
| **Gradient Accumulation** | `4` (for small GPUs)      |
| **Scheduler**             | `cosine`                  |
| **Compute Type**          | `bf16` (for modern GPUs)  |

**Step 5: Start Training**

* Click **Start** to launch fine-tuning.
* Monitor logs and **loss curves** to track progress.

<figure><img src="../.gitbook/assets/Screenshot 2025-02-18 at 13.31.08.png" alt=""><figcaption></figcaption></figure>

### 3. Chat

After the model finishes training, you can move to the Chat tab and follow the steps below:

* select the model&#x20;
* select the checkpoint you want to test
* write your query in the Input section and submit the query

Here you can try the model out. As you can see below, it has already started showing reasoning:

<figure><img src="../.gitbook/assets/Screenshot 2025-02-24 at 18.01.38 (1).png" alt=""><figcaption></figcaption></figure>

After it finishes, you can expand the **Though** section to see all of the reasoning tokens.

<figure><img src="../.gitbook/assets/Screenshot 2025-02-25 at 18.58.06.png" alt=""><figcaption></figcaption></figure>

### 4. Evaluating Your Fine‐Tuned/Trained Model

Once your training (or fine‐tuning) has completed, you can **evaluate** the new model from within the Web UI:

1. **Navigate to the “Evaluate & Predict” Tab**\
   From the top menu in LLaMA Factory (Train / Evaluate & Predict / Chat / Export), click **Evaluate & Predict**.
2. **Select Your Checkpoint**
   * **Model name**: Choose the same base model used for fine‐tuning (e.g., `Llama-3.2-3B` ).
   * **Checkpoint path**: Pick the checkpoint directory you just trained (e.g., `train_2025-02-17-12-36-51`).
3. **Configure the Dataset for Evaluation**
   * **Data dir**: Set to the directory containing your dataset files (e.g., `data`).
   * **Dataset**: Select the dataset entry you want to evaluate on (e.g., `open-r1/OpenR1-Math-220k`).
   * Use the **Preview dataset** button (optional) to confirm that the dataset is recognized properly (e.g., no `'from'` KeyError, or other format issues).
4. **Adjust Evaluation Settings**
   * **Cutoff length**: The maximum token length in your input sequences (e.g., 1024).
   * **Max samples**: How many data samples to evaluate (e.g., 1000).
   * **Batch size**: The number of samples processed simultaneously per GPU (e.g., 2 or 4, depending on GPU memory).
   * **Save predictions**: Tick this box to store the model outputs on each sample.
   * **Maximum new tokens**: How many tokens the model may generate for each example (e.g., 512).
   * **Top‐p** and **Temperature**: Sampling hyperparameters—adjust for different sampling behaviors (e.g., `top_p=0.7`, `temperature=0.95`).
   * **Output dir**: Where the evaluation logs and predictions will be saved.
5. **Start the Evaluation**
   * Click **Start**.
   * Monitor logs in the console below the Start button.
   * Once finished, LLaMA Factory will show the evaluation progress and any metrics (if the dataset has built‐in metrics).
   * If **Save predictions** was checked, look for a file (e.g., `.jsonl` or `.csv`) in the `output` directory with each sample’s output.
6. **Review Results**
   * If your dataset or LLaMA Factory supplies metrics (like accuracy, perplexity, or F1), they will appear in the logs or console.
   * You can also open the saved predictions file to see the raw completions on each sample.

> **Tip**: If your dataset does not provide built‐in metrics, you will see only raw predictions. You can parse these to do custom scoring if needed.

<figure><img src="../.gitbook/assets/Screenshot 2025-02-26 at 15.40.05.png" alt=""><figcaption></figcaption></figure>

Final results will be visible after the evaluation finishes, it's a good practice to evaluate model you're starting off with and then evaluate the fine-tuned/trained one so you can understand if results improved or not.

<figure><img src="../.gitbook/assets/Screenshot 2025-02-26 at 16.14.18.png" alt=""><figcaption></figcaption></figure>

### 5. Exporting the model&#x20;

For exporting models, you need to switch to the export tab and follow these steps:&#x20;

* Set the export dir (where you want the model to be saved in the mapped volume); you can later download it from this directory; it's recommended to be under one of the mounted volumes in the `.apolo/live.yaml`&#x20;

```yaml
output:
  remote: storage:$[[ flow.project_id ]]/output
  mount: /app/saves
  local: output
```

* you can also provide the HF Hub ID, if you want the model to be uploaded to that Huggingface Repo

<figure><img src="../.gitbook/assets/Screenshot 2025-02-25 at 19.09.52.png" alt=""><figcaption></figcaption></figure>

After exporting the model on Huggingface, you can deploy it also using the vLLM app






















---
File: /use-cases/visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai/architecture-overview.md
---

# Architecture Overview

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXffGeCkD5bNWgCEHL758pzDWfp7e97AzzSWqUz7EpZ8WeWkfsPZYUsA6-I1uY25tV6hWQvvFQPvbB-1eLJBxBS6HD1VJBE4GVmLVTAq1mNgqhu3gucBgk25O-6904W-Kq9R2GznEQ?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

The Visual RAG pipeline consists of the following key components:

1. **Data Ingestion**: PDFs are uploaded to Apolo’s object storage and processed by a job that uses **ColPali** to generate embeddings for text and images.
2. **Storage**:

* **LanceDB** serves as the vector database for storing embeddings.
* Apolo’s storage backend is used to persist raw data and intermediate outputs.

3. **Query Handling**:

* User queries are embedded using **ColPali**.
* LanceDB retrieves the most relevant PDF pages (text and image embeddings).

4. **Response Generation**: A visual LLM takes retrieved pages and the user query as input, generating a comprehensive answer.
5. **Visualization**: Results are displayed via a Streamlit dashboard, showing the top-matched images and the LLM’s response.



---
File: /use-cases/visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai/implementation.md
---

# Implementation

### **1. Setting Up Apolo**

```
pip install apolo-all
apolo login
apolo config show
```

The Apolo platform is the backbone of this workflow, providing:

* **Compute Resources**: GPUs for running ML models.
* **Storage**: To manage raw data, embeddings, and processed outputs.
* **Job Management**: To orchestrate the pipeline.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfaH0FBw4EzsaRPwu1Xu1m_2_MeWvt-f743mEZ0RJ6etWIibw-u_qE0f03XZrWduwdayE6yAQqy7cqwWKCzH65jmCuq23V6k5JU4EbErxpTXGN9iV5H6TjfSrxHurAxY116SbjG?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

### **2. Data Preparation**

**Upload your sample data to Apolo:**

```
apolo cp -r ./sample_data/ storage:visual_rag/raw-data/
```

The uploaded PDFs will **be used to extract text and images for embedding.**

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKbuusGG-ikw2voPQVrEXrt5YOD3YLMYclklA6O7lMpy_gANTpkA2l_IHosOWziWWok6vJCoukHnVU6QOOh8KvwXrRZ7eDfprK5kIavx6UHNxfE6O9Oju0tLPM-7-abjMvWHYp?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeQoMmO_wFn6yBI-U5U32AOt67XZoskMQnss6WYh_jaATmvdKjFYCFj21ZtHwEsDyP2Dq9mPjAR1Id3FJNnlWzI2s-hLUAfWIDOqXoC0nHtp2sytkrtrkCqaPEDOOS7SAx4CKLH?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

### **3. Data Ingestion**

Run the ingestion job to process PDFs and store embeddings in LanceDB:

```
apolo run --detach \
          --no-http-auth \
          --preset H100x1 \
          --name ingest-data \
          --http-port 80 \
          --volume storage:visual_rag/cache:/root/.cache/huggingface:rw \
          --volume storage:visual_rag/raw-data/:/raw-data:rw \
          --volume storage:visual_rag/lancedb-data/:/lancedb-data:rw \
          -e HF_TOKEN=$HF_TOKEN \
          ghcr.io/kyryl-opens-ml/apolo_visual_rag:latest -- python main.py ingest-data /raw-data --table-name=demo --db-path=/lancedb-data/datastore
```

The ingestion process involves:

* Extracting images and text from each page of a PDF.
* Generating embeddings for these components using **ColPali**.
* Storing the embeddings in LanceDB.

```python
def ingest_data(folder_with_pdfs: str, table_name: str = "demo", db_path: str = "lancedb"):
    model, processor = get_model_colpali()

    pdfs = [x for x in Path(folder_with_pdfs).iterdir() if x.name.endswith('.pdf')]
    print(f"Input PDFs {pdfs}")

    for pdf_path in tqdm(pdfs):
        print(f"Getting images and text from {pdf_path}")
        page_images, page_texts = get_pdf_images(pdf_path=pdf_path)
        print(f"Getting embeddings from {pdf_path}")
        page_embeddings = get_images_embedding(images=page_images, model=model, processor=processor)
        print(f"Adding to db {pdf_path}")
        table = add_to_db(pdf_path=pdf_path, page_images=page_images, page_texts=page_texts, page_embeddings=page_embeddings, table_name=table_name, db_path=db_path)
        print(f"Done! {pdf_path} should be in {table} table.")
    print("All files are processed")
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdx37HCyEp6-tatgzCjSWKCeKdTZNRAPawAhRhCVxuR0ZEatXXxc5bNDTjjjRZGnc50KcTQhmmEK7d1H6B9p40zUvkcSeNR1rOjLhq1Pcb_AcKxwea_uao3xdfP2hasqBcOP-6i?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeH0ry6DD8zElpSvlvVIVApNGM3mE_ktYZ7Q6nWW7d_4-4kA99R-QPWXwNBguefK_YZgS8DDViIKQM_0CBW_shlahOOsFJYd6ONmHBTE8WuRLqsro4fTjn8UQV3wFjxR1Dhx2QI-g?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

The processed data, including embeddings and metadata, is stored in **LanceDB**, a vector database optimized for high-speed search and retrieval.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdAgXCUsQ6H1pCo8OktC5aHo3S6hzmHkMZXNDp57EXcwf-goqdi1A0_qtm_53oh3h3ScYpNezm0pCfDLtrXUwmKJm2NZoCeFyrjL-6S7rzEuZYPK7aRVyll_JAacYHKYy0zs48x?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

### **4. Deploy the Generative LLM**

Once the data is ingested and stored in LanceDB, deploy the generative LLM server for processing multimodal queries. This server runs the **Llama 3.2 Vision-Instruct** model, enabling responses based on both text and visual data.

```
apolo run --detach \
          --no-http-auth \
          --preset H100x1 \
          --name generation-inference \
          --http-port 80 \
          --volume storage:visual_rag:/models:rw \
          -e HF_TOKEN=$HF_TOKEN \
          ghcr.io/huggingface/text-generation-inference:2.4.0 -- --model-id meta-llama/Llama-3.2-11B-Vision-Instruct

```

**What Happens in This Step:**

* **Deploying the Server**: The command sets up the generative LLM server within Apolo’s infrastructure, running the `meta-llama/Llama-3.2-11B-Vision-Instruct` model.
* **Secure Storage Integration**: The model weights are accessed securely via the mounted `storage:visual_rag` directory.
* **Multimodal Inference**: The server is configured to handle multimodal queries, such as combining text and images for processing.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd6PPgGg8zoE60uZQz5Q0uHmzNUw-i7HYLK3b-Y3jSun3UrFv7r2N_FL-H9awctcuNiqU0V0yrt-XMuBctv7Ngd0hIdX1kj_2YPPB_Rj5q35gJR2vFBzocy9LgaWm334w10SDJI6g?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

With this setup, your generative LLM is ready to serve multimodal queries, providing the backbone for the Visual RAG pipeline. The system can now combine the embeddings retrieved from LanceDB with the user queries, using the model to generate comprehensive and accurate responses.

### **5. Querying the System**

With the ingestion pipeline and LLM server running, you can query the system using the `ask_data` function:

```python
def ask_data(user_query = "What is market share by region?", table_name: str = "demo", db_path: str = "lancedb", base_url: str = "http://generation-inference--9771360698.jobs.scottdc.org.neu.ro/v1", top_k: int = 5):
    model, processor = get_model_colpali()
    print(f"Asking {user_query} query.")

    print("1. Search relevant images")
    query_embeddings = get_query_embedding(query=user_query, model=model, processor=processor)
    results = search_db(query_embeddings=query_embeddings, processor=processor, db_path=db_path, table_name=table_name, top_k=top_k)
    print(f"result most relevant {results}")

    print("2. Build prompt")
    # https://cookbook.openai.com/examples/custom_image_embedding_search#user-querying-the-most-similar-image
    prompt = f"""
    Below is a user query, I want you to answer the query using images provided.
    user query:
    {user_query}
    """    
    print(f"Prompt = {prompt}")
    print("3. Query LLM with prompt and relavent images")
    input_images = [results[idx]['pil_image'] for idx in range(top_k)]
    llm_response = run_vision_inference(input_images=input_images, prompt=prompt, base_url=base_url)
    print(f"llm_response {llm_response}")
```

**Here’s how it works:**

1. **Query Embedding**: The user query is embedded using ColPali in `get_query_embedding`.
2. **Database Search**: `search_db` retrieves the most relevant images based on embeddings.
3. **Response Generation**: A vision-enabled LLM (e.g., Llama 3.2) processes the prompt and images via `run_vision_inference`.

### **6. Visualizing the Results**

To enhance usability, integrate a Streamlit-based dashboard for querying and visualizing responses. The dashboard includes:

* **PDF Viewer**: Displays available documents for context.
* **Search Input**: Allows users to submit natural language queries.
* **Results Panel**: Shows the retrieved images and the LLM-generated responses.

For example, querying “What is the market share by region?” retrieves visuals related to market share and generates a concise, context-aware response.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf74Ea4_stBchPF3hRF8sR3vXXpqHcqgPr7cTpCJSzFW8k6fXDUHnKmGAOAKghUTaOm7569JjfOWLIKZ7tr9_rg3Z280JOJRPihuuvwQR9VDenVl64slxISV8ggDYv8ZjfOy6SdBQ?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>



---
File: /use-cases/visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai/README.md
---

# Visual RAG on Complex PDFs: Enterprise-Ready Multimodal AI



{% embed url="https://www.loom.com/share/29bea291db4c48f9ae74ef1377a2dafd" %}



{% embed url="https://github.com/neuro-inc/apolo-reference-architectures" %}

Building enterprise-ready generative AI applications is more than just deploying an LLM; it’s about ensuring **security**, **performance**, and the ability to handle complex, real-world data. Today, we dive into **Visual Retrieval-Augmented Generation (RAG)** for complex PDF documents using the **Apolo platform**, showcasing how to extract actionable insights from visually rich documents.

This guide demonstrates how to build a **Visual RAG** application on Apolo.&#x20;

Here’s **what makes it enterprise-ready**:

1. **Security**: All data stays within your controlled environment with full monitoring and auditability.
2. **Performance**: Comparable to top-tier LLM services like OpenAI but running entirely on-premises for complete autonomy.

For this project, we leverage:

* **Llama 3.2 Vision**: A generative LLM with multimodal capabilities.
* **ColPali**: A cutting-edge visual embedder for processing complex documents.
* **LanceDB**: A lightweight, Rust-based vector database seamlessly integrated with Apolo’s object storage.

By combining these tools, we build a system that processes **complex PDFs with images**, **plots**, and **tables**, enabling natural language queries with visual understanding.

### Why Visual RAG?

Traditional RAG systems rely on text-based embeddings, but many enterprise documents, such as **financial reports, technical manuals, and research papers**, contain critical information embedded in visuals. Traditional OCR-based methods struggle with:

* Parsing complex layouts and relationships between text and visuals.
* Processing rich, interdependent plots and tables.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHJBbkxo_Yap-no-_2Px9QajaHRfaXmy27FWFxaQx5X_DJICVloJqCRgApU5wONyvW9SRYxXBIstE-NCR9nhbyRhBhgDJyrHPSsAVLcBOjDMRgfRyTP6HHBf5_IQk62CdXTtS3xg?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

The **ColPali** model eliminates this bottleneck by embedding entire document pages - text and visuals combined - into vectors. Paired with **Llama 3.2 Vision**, a multimodal large language model (LLM), it enables precise question answering across complex, visually rich documents.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfWCmCbDOGPUTlusiNtEU7AzXMAo0aE_SoxVo7KarSYFsFGMDgyF3wRsOZ-b3d0XbRPrTt6LfqLxofqHw-o276EJQ07lWo5E7zbG3tnIEGSKxG-fxaZkCKPsClrAtEoaRf1OXIQng?key=otIZGGH9IV7FtNlKEVwhAb5T" alt=""><figcaption></figcaption></figure>

### Advantages:

1. **Security & Performance**: The entire pipeline runs on-premise, ensuring data security while maintaining high throughput.
2. **Scalability**: Apolo’s platform supports seamless scaling for processing large datasets.
3. **State-of-the-Art Technology**: By integrating ColPali, LanceDB, and Llama 3.2 Vision-Instruct, the system achieves best-in-class document understanding.

**Future developments may include:**

* Fine-tuning the LLM for domain-specific use cases.
* Expanding support for additional document types.
* Optimizing query performance with more advanced retrieval methods.

Visual RAG on Apolo demonstrates how modern AI can transform document processing for enterprises. By leveraging multimodal LLMs, vector databases, and scalable infrastructure, this system sets a new standard for handling unstructured data.

If you’re interested in exploring this further, feel free to contact us ([start@apolo.us](mailto:start@apolo.us)) for a demo or check out [the code on GitHub](https://github.com/neuro-inc/apolo-reference-architectures).



---
File: /use-cases/README.md
---

# Enterprise-Ready Generative AI Applications

{% embed url="https://www.loom.com/share/b5ed68d7f60b4fd6a987e19242832571" %}



{% embed url="https://github.com/neuro-inc/apolo-reference-architectures" %}

Generative AI has transformed the way enterprises interact with data, but creating enterprise - grade applications demands exceptional **security** and **performance**. In this blog, we explore how to build **Retrieval-Augmented Generation (RAG)** applications using the Apolo **platform**, leveraging its on-premise capabilities and industry-leading tools.

Whether you're querying financial data or building a chatbot for enterprise documentation, Apolo streamlines the process, allowing developers to focus on innovation.

### **Enterprise-Ready: What Does It Mean?** <a href="#ose5ahiya5fo" id="ose5ahiya5fo"></a>

Enterprise-ready solutions prioritize:

1. **Security**: Complete data privacy - nothing leaves your environment, ensuring full control.
2. **Performance**: Comparable with leading AI models like OpenAI, Anthropic, and Meta models.

Apolo’s platform combines these pillars with the flexibility to run **Llama 3.1 models** (ranging from 8B to 70B parameters), making it an ideal choice for building scalable, secure, and high-performing generative AI applications.

### **Understanding RAG and the Apolo Platform** <a href="#kt964uhkje38" id="kt964uhkje38"></a>

Retrieval-Augmented Generation (RAG) enhances the quality of generative AI applications by combining powerful LLMs with structured retrieval systems. Here’s how it works:

1. **Generative LLM**: Generates responses by interpreting input text.
2. **Embedding LLM**: Converts text into numerical embeddings for efficient similarity searches.
3. **Re-ranker LLM**: Scores and ranks retrieved data for relevance.

Additionally, RAG applications require:

* **Retrieval Database**: For efficient storage and querying of embeddings (e.g., PostgreSQL with PGVector).
* **Data Moat**: Continuous improvement through user feedback, stored and analyzed in tools like Argilla.

The Apolo platform simplifies these complexities by offering:

* **Apolo CLI**: Streamline operations via command-line management.
* **Apolo Storage**: Secure and scalable data storage.
* **Apolo Jobs**: GPU-powered infrastructure for high-performance model operations.
* **Apolo UI**: A user-friendly interface for visualizing workflows.

![](.gitbook/assets/0.png)

![](.gitbook/assets/1.png)

The two case studies - **Apolo Documentation Chatbot** and **Canada Budget Chatbot** - demonstrate the versatility and power of RAG architectures on the **Apolo platform**.&#x20;

By combining:

* Secure, on-premise infrastructure.
* High-performance generative AI models.
* Advanced retrieval mechanisms powered by PostgreSQL, vector embeddings, and LLMs.
* Feedback-driven iterative improvements with Argilla.

The Apolo platform enables the development of enterprise-ready generative AI applications.

#### **Key Takeaways** <a href="#gbeu3mkyuw1y" id="gbeu3mkyuw1y"></a>

* **Enterprise-grade capabilities**: Apolo ensures data security and high performance, meeting the stringent demands of enterprise use cases.
* **Customizable architectures**: The modular RAG setup can be tailored for different domains, from technical documentation to financial analysis.
* **Iterative refinement**: Feedback loops drive continuous improvement, enhancing both the user experience and system accuracy.

Whether you’re building a chatbot to navigate complex corporate documentation or to provide insights from voluminous data like budgets, the Apolo platform offers a seamless path to creating scalable, efficient, and secure generative AI applications.

If you’re interested in exploring this further, feel free to contact us ([start@apolo.us](mailto:start@apolo.us)) for a demo or check out [the code on GitHub](https://github.com/neuro-inc/apolo-reference-architectures).



---
File: /use-cases/SUMMARY.md
---

# Table of contents

* [Enterprise-Ready Generative AI Applications](README.md)
  * [Apolo Documentation Chatbot](enterprise-ready-generative-ai-applications/apolo-documentation-chatbot.md)
  * [Canada Budget RAG](enterprise-ready-generative-ai-applications/canada-budget-rag.md)
* [Visual RAG on Complex PDFs: Enterprise-Ready Multimodal AI](visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai/README.md)
  * [Architecture Overview](visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai/architecture-overview.md)
  * [Implementation](visual-rag-on-complex-pdfs-enterprise-ready-multimodal-ai/implementation.md)

## Generic

* [ML Model Lifecycle on Apolo Platform](generic/ml-model-lifecycle-on-apolo-platform/README.md)
  * [End-to-End ML Model Lifecycle using Apolo CLI](generic/ml-model-lifecycle-on-apolo-platform/end-to-end-ml-model-lifecycle-using-apolo-cli.md)
  * [ML Model Lifecycle using Apolo Console](generic/ml-model-lifecycle-on-apolo-platform/ml-model-lifecycle-using-apolo-console.md)

## Large language models <a href="#llms" id="llms"></a>

* [DeepSeek-R1 distilled models](llms/deepseek-r1-distilled-models.md)
* [DeepSeek-R1 model deployment](llms/deepseek-r1-model-deployment.md)
* [Teaching Models To Reason - Training, Fine-Tuning, and Evaluating Models with LLaMA Factory on Apolo](llms/teaching-models-to-reason-training-fine-tuning-and-evaluating-models-with-llama-factory-on-apolo.md)
* [Autonomous Research with AgentLaboratory: DeepSeek R1 vs. OpenAI o1](llms/autonomous-research-with-agentlaboratory-deepseek-r1-vs.-openai-o1.md)

## Image and Video processing

* [Synthetic Data Generation using Stable Diffusion](image-and-video-processing/synthetic-data-generation-using-stable-diffusion.md)
* [HOWTO: Lora models with Stable Diffusion](image-and-video-processing/howto-lora-models-with-stable-diffusion.md)

